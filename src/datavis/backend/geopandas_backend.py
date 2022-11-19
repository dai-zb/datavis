from .matplotlib_backend import MatplotlibPlotBackend
from ..config import FigCfg, AxCfg, PlotCfg

from typing import Optional, Union, List, Sequence

try:
    import geopandas as gpd
except ImportError:
    pass


class GeopandasBackend(MatplotlibPlotBackend):
    def __init__(self, fig_cfg: Optional[FigCfg] = None, ax_cfg: Optional[AxCfg] = None):
        super().__init__(fig_cfg, ax_cfg)

    def geojson(self, path, idx: int = 0,
                label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        geo = gpd.read_file(path)
        kwargs = {}
        if "color" in _cfg:
            kwargs["edgecolor"] = _cfg["color"]
        if "facecolor" in _cfg:
            kwargs["color"] = _cfg["facecolor"]
        geo.plot(ax=self.get_ax(idx), **kwargs)

    # 以下方法不希望在 geopandas 的backend中使用 =======================
    def bar(self, x, y, bottom=None, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def pie(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def stack_plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                   cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def hist(self, x, bins, density=False, cumulative=False,
             idx: int = 0, label: Optional[str] = None,
             cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def radar(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
              cfg: Optional[PlotCfg] = None):  # 雷达图
        raise NotImplementedError()

    def box_plot(self, x, vert=False,
                 idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def violin_plot(self, x, vert=False,
                    idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                    cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def im_show(self, img, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def gantt(self, datas: Sequence[Sequence], delta_date: int, idx: int = 0,
              label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        # #甘特图 #gantt
        raise NotImplementedError()
