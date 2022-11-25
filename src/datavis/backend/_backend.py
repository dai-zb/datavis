from ..config import FigCfg, AxCfg, PlotCfg, LegendCfg

from typing import Optional, List, Union, Tuple, Sequence
from abc import abstractmethod


# idx   �������
# label ��һЩ�����У��������û��ʹ�õ������Ǳ�����ڣ���Ϊ��ʽ��Ҫ

class Backend:
    @abstractmethod
    def __init__(self,
                 fig_cfg: Optional[FigCfg] = None,
                 ax_cfg: Optional[AxCfg] = None):
        pass

    def __call__(self, x, y, idx: int = 0, label: Optional[str] = None,
                 cfg: Optional[PlotCfg] = None):
        self.plot(x, y, idx, label, cfg)

    def plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
             cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def fill_between(self, x, y1, y2=0, where: Optional[List[bool]] = None,
                     idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def bar(self, x, y, bottom=None, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def error_bar(self, x, y, x_err=0, y_err=0, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                  cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def pie(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def stack_plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                   cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def scatter(self, x, y, s=None, c=None, idx: int = 0, label: Optional[str] = None,
                cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def hist(self, x, bins, density=False, cumulative=False,
             idx: int = 0, label: Optional[str] = None,
             cfg: Optional[PlotCfg] = None):
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

    def add_box(self, box, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def mask(self, x: List[Tuple[float, float]], idx: int = 0, label: Optional[Union[str, List[str]]] = None,
             cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    def mat_show(self, mat, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()
		
	def geojson(self, path, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        raise NotImplementedError()

    @abstractmethod
    def get_ax(self, idx: int = 0, twin_x: bool = False, twin_y: bool = False):
        raise NotImplementedError()

    @abstractmethod
    def ax_set(self, idx: int = 0, cfg: Optional[AxCfg] = None):
        raise NotImplementedError()

    @abstractmethod
    def legend_set(self, idx: int = 0, cfg: Optional[LegendCfg] = None):
        raise NotImplementedError()

    @abstractmethod
    def show(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, path: str):
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        raise NotImplementedError()
