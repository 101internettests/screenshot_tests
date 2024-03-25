from PIL import ImageDraw, Image
from io import BytesIO
from typing import Union, List


class ImageProcessor:

    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    ALPHA = "alpha"

    TOLERANCE = {
        RED: 16,
        GREEN: 16,
        BLUE: 16,
        ALPHA: 16,
    }

    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 20

    @staticmethod
    def load_image_from_bytes(data: bytes) -> Image.Image:
        """Загрузить изображение из байтовой строки."""
        with BytesIO(data) as fp:
            image: Image.Image = Image.open(fp)
            image.load()
            return image

    @staticmethod
    def image_to_bytes(image: Image.Image) -> bytes:
        with BytesIO() as fp:
            image.save(fp, "PNG")
            return fp.getvalue()

    def is_color_similar(self, a, b, color):
        """Проверить похожесть цветов. Для того чтобы тесты не тригеррились на антиалиазинг допуски
        в self.TOLERANCE.
        """
        if a is None and b is None:
            return True
        diff = abs(a - b)
        if diff == 0:
            return True
        elif diff < self.TOLERANCE[color]:
            return True
        return False

    def compare_pixels(self, pixel_one, pixel_two) -> bool:
        """Сравнить каждый цвет, каждого пикселя."""
        assert len(pixel_one) == len(pixel_two), f"В одном из пикселей не хватает цветов: {pixel_one} {pixel_two}"
        for item in zip(pixel_one, pixel_two, (self.RED, self.GREEN, self.BLUE, self.ALPHA)):
            color_one, color_two, color = item
            if not self.is_color_similar(color_one, color_two, color):
                return False
        return True

    def compare_images(self, image_one: Image.Image, image_two: Image.Image) -> bool:
        """Сравнить два изображения попиксельно"""
        assert image_one.size == image_two.size, \
            f"Картинки должны быть одинакового размера, {image_one.size} {image_two.size}"
        max_width, max_height = image_one.size
        for coord_y in range(0, max_height):
            for coord_x in range(0, max_width):
                pixel_one = image_one.getpixel((coord_x, coord_y))
                pixel_two = image_two.getpixel((coord_x, coord_y))
                equal = self.compare_pixels(pixel_one, pixel_two)
                if not equal:
                    return False
        return True

    def slice_image(self, image: Image.Image) -> List[dict]:
        """Нарезать картинки на блоки"""
        max_width, max_height = image.size
        width_change = self.BLOCK_WIDTH
        height_change = self.BLOCK_HEIGHT
        result = []
        for row in range(0, max_height, self.BLOCK_HEIGHT):
            for col in range(0, max_width, self.BLOCK_WIDTH):
                if width_change > max_width:
                    width_change = max_width
                if height_change > max_height:
                    height_change = max_height
                box = (col, row, width_change, height_change)
                cropped = image.crop(box)
                result.append({"image": cropped, "box": box})
                width_change += self.BLOCK_WIDTH
            height_change += self.BLOCK_HEIGHT
            width_change = self.BLOCK_WIDTH
        return result

    def check_images_difference(self, first_image: Image.Image, second_image: Image.Image) -> List[Union[int, bytes]]:
        """Поблочно сравнить два изображения и вернуть количество блоков с не совпавшими пикселями"""
        result_image = first_image.copy()
        first_image_blocks = self.slice_image(first_image)
        second_image_blocks = self.slice_image(second_image)
        mistaken_blocks = abs(len(first_image_blocks) - len(second_image_blocks))
        for index in range(min(len(first_image_blocks), len(second_image_blocks))):
            image_equal = self.compare_images(first_image_blocks[index]["image"], second_image_blocks[index]["image"])
            if not image_equal:
                draw = ImageDraw.Draw(result_image)
                draw.rectangle(first_image_blocks[index]["box"], outline="red")
                mistaken_blocks += 1
        return [mistaken_blocks, self.image_to_bytes(result_image)]