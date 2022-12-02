from .backend import MatplotlibPlotBackend, GeopandasBackend
from .config import FigCfg, AxCfg, PlotCfg, LegendCfg
from .backend import Backend
from .calc import linear_regression, norm_distribution_quantile

from typing import Optional, List, Union, Tuple, Sequence

_map = {
    "matplotlib": MatplotlibPlotBackend,
    "geopandas": GeopandasBackend,
}


class Plot(Backend):
    def __init__(self,
                 fig_cfg: Optional[FigCfg] = None,
                 ax_cfg: Optional[AxCfg] = None,
                 backend="matplotlib"
                 ):
        super().__init__(fig_cfg, ax_cfg)
        self.backend = _map[backend](fig_cfg=fig_cfg, ax_cfg=ax_cfg)

    def reg_plot(self, x, y, s=None, c=None, order: int = 1, idx: int = 0, label: Optional[str] = None,
                 cfg: Optional[PlotCfg] = None) -> List[float]:

        self.scatter(x, y, s, c, idx, label, cfg)
        w = linear_regression(x, y, order)[:: -1]

        def _fun(z):
            ret = 0
            for n, _w in enumerate(w):
                ret += _w * (z ** n)
            return ret

        y_ = [_fun(item) for item in x]
        self.plot(x, y_, idx, label, cfg)
        # y = w3*x^3 w2*x^2 + w1*x + w0
        # w3, w2, w1, w0
        return w
    
    """
    def speed_2_soc(s):
        w = [0.0034903080840019913, 0.0032917914210580735, -8.276159402025737e-05, 3.3147479342491715e-06,
             -4.11750452428776e-08, 1.9666554175741654e-10]

        ret = 0
        n = len(w)
        for i in range(n):
            ret += w[i] * s ** i

        return ret
    """

    def q_q_plot(self, data, dist=None, s=None, c=None, idx: int = 0, label: Optional[str] = None,
                 cfg: Optional[PlotCfg] = None) -> Tuple[float, float]:
        # Q-Q图是基于分位数的，P-P图是基于累积分布的
        if dist is None:
            n = len(data)
            _dist = [norm_distribution_quantile((i + 1) / (n + 1)) for i in range(n)]
        else:
            _dist = dist.copy()
            _dist.sort()
        _data = data.copy()
        _data.sort()

        self.scatter(_dist, _data, s, c, idx, label, cfg)

        k, b = linear_regression(_dist, _data)
        _data2 = [k * item + b for item in _dist]

        self.plot(_dist, _data2, idx, label, cfg)
        return k, b

    def plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
             cfg: Optional[PlotCfg] = None):
        return self.backend.plot(x, y, idx, label, cfg)

    def fill_between(self, x, y1, y2=0, where: Optional[List[bool]] = None,
                     idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        return self.backend.fill_between(x, y1, y2, where, idx, label, cfg)

    def bar(self, x, y, bottom=None, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        return self.backend.bar(x, y, bottom, idx, label, cfg)

    def error_bar(self, x, y, x_err=0, y_err=0, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                  cfg: Optional[PlotCfg] = None):
        return self.backend.error_bar(x, y, x_err, y_err, idx, label, cfg)

    def pie(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        return self.backend.pie(x, y, idx, label, cfg)

    def stack_plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                   cfg: Optional[PlotCfg] = None):
        return self.backend.stack_plot(x, y, idx, label, cfg)

    def scatter(self, x, y, s=None, c=None, idx: int = 0, label: Optional[str] = None,
                cfg: Optional[PlotCfg] = None):
        return self.backend.scatter(x, y, s, c, idx, label, cfg)

    def hist(self, x, bins, density=False, cumulative=False,
             idx: int = 0, label: Optional[str] = None,
             cfg: Optional[PlotCfg] = None):
        return self.backend.hist(x, bins, density, cumulative, idx, label, cfg)

    def radar(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
              cfg: Optional[PlotCfg] = None):  # 雷达图
        return self.backend.radar(x, y, idx, label, cfg)

    def box_plot(self, x, vert=False,
                 idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        return self.backend.box_plot(x, vert, idx, label, cfg)

    def violin_plot(self, x, vert=False,
                    idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                    cfg: Optional[PlotCfg] = None):
        return self.backend.violin_plot(x, vert, idx, label, cfg)

    def im_show(self, img, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                cfg: Optional[PlotCfg] = None):
        return self.backend.im_show(img, idx, label, cfg)

    def add_box(self, box, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        return self.backend.add_box(box, idx, label, cfg)

    def mask(self, x: List[Tuple[float, float]], idx: int = 0, label: Optional[Union[str, List[str]]] = None,
             cfg: Optional[PlotCfg] = None):
        return self.backend.mask(x, idx, label, cfg)

    def mat_show(self, mat, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        return self.backend.mat_show(mat, idx, label, cfg)

    def geojson(self, path, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        return self.backend.geojson(path, idx, label, cfg)

    def gantt(self, datas: Sequence[Sequence], delta_date: int, idx: int = 0,
              label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        # #甘特图 #gantt
        return self.backend.gantt(datas, delta_date, idx, label, cfg)

    def get_ax(self, idx: int = 0, twin_x: bool = False, twin_y: bool = False):
        return self.backend.get_ax(idx)

    def ax_set(self, idx: int = 0, cfg: Optional[AxCfg] = None):
        return self.backend.ax_set(idx, cfg)

    def legend_set(self, idx: int = 0, cfg: Optional[LegendCfg] = None):
        return self.backend.legend_set(idx, cfg)

    def save(self, path: str):
        return self.backend.save(path)

    def show(self):
        return self.backend.show()

    def close(self):
        return self.backend.close()
