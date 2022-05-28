from pygame import Vector2


class Codec:
    @staticmethod
    def encode_vec2(vec: Vector2) -> dict:
        return {
            "x": vec.x,
            "y": vec.y
        }

    @staticmethod
    def decode_vec2(data: dict) -> Vector2:
        return Vector2(data.get("x"), data.get("y"))
