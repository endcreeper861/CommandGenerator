class Selector:
    """目标选择器"""

    def __init__(
        self,
        var: str,
        x: float | None = None,
        y: float | None = None,
        z: float | None = None,
        distance: str | None = None,
        dx: int | None = None,
        dy: int | None = None,
        dz: int | None = None,
    ) -> None:
        """创建新的目标选择器"""
