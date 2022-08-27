from ._backend import Backend
from ..config import FigCfg, AxCfg, LegendCfg, PlotCfg

from matplotlib import pyplot as plt
from numpy import ndarray

from typing import Optional, List, Union, Tuple

from ..style import Markers

_fig_method_map = {
    # 参数名称: cfg中对应的key
    "figsize": "figure_size",
    "nrows": "figure_rows_number",
    "ncols": "figure_columns_number",
    "sharex": "share_x_axis",
    "sharey": "share_y_axis",
    "tight_layout": "tight_layout",
}

_ax_method_map = {
    # 方法名称 : { 参数名称: cfg中对应的key }
    "set_title": {"label": "title", "fontsize": "title_font_size"},
    "set_xlabel": {"xlabel": "x_label", "fontsize": "label_font_size"},
    "set_ylabel": {"ylabel": "y_label", "fontsize": "label_font_size"},
    "grid": {"linestyle": "grid"},

    "set_xlim": {"left": "x_limit_left", "right": "x_limit_right"},
    "set_ylim": {"bottom": "y_limit_bottom", "top": "y_limit_top"},

    "set_xticks": {"ticks": "x_ticks", "labels": "x_tick_labels", "rotation": "x_tick_rotation",
                   "fontsize": "tick_font_size"},
    "set_yticks": {"ticks": "y_ticks", "labels": "y_tick_labels", "rotation": "y_tick_rotation",
                   "fontsize": "tick_font_size"},
}

_arg_name_map = {

    "color": "color",
    "face_color": "facecolor",

    "marker": "marker",
    "marker_size": "markersize",
    "line_style": "linestyle",
    "line_width": "linewidth",
    "colormap": "cmap",

    "location": "loc",
    "columns_number": "ncol",

    "hist_type": "histtype",

    "font_size": "fontsize"
}


def _arg_rename_all(d: dict):
    _d = {}
    for k, v in d.items():
        if _arg_name_map.get(k) is not None:
            k = _arg_name_map[k]
        _d[k] = v
    return _d


def _arg_rename(d: dict, old_key: str, new_key: str):
    if old_key in d:
        d[new_key] = d.pop(old_key)
    return d


class MatplotlibPlotBackend(Backend):
    def __init__(self, fig_cfg: Optional[FigCfg] = None, ax_cfg: Optional[AxCfg] = None):
        super().__init__(fig_cfg, ax_cfg)
        if fig_cfg is not None:
            _fig_cfg = fig_cfg.matplotlib
            args = {k: _fig_cfg[v] for k, v in _fig_method_map.items() if v in _fig_cfg}
            fig, axs = plt.subplots(**args)

            kwargs = {x: _fig_cfg[x] for x in ["h_space", "w_space"]
                      if _fig_cfg.get(x) is not None}
            kwargs = _arg_rename(kwargs, "h_space", "hspace")
            kwargs = _arg_rename(kwargs, "w_space", "wspace")
            if kwargs:
                fig.subplots_adjust(**kwargs)
        else:
            fig, axs = plt.subplots()
        if isinstance(axs, ndarray):
            self.axs = axs.flatten()
        else:
            self.axs = (axs,)

        self.axs_twin_x: dict = {}  # 双轴 共用x轴
        self.axs_twin_y: dict = {}  # 双轴 共用x轴

        self.fig = fig

        for idx in range(len(self.axs)):
            self.ax_set(idx, ax_cfg)

    def get_ax(self, idx: int = 0, twin_x: bool = False, twin_y: bool = False):
        ax = self.axs[idx]

        if twin_x:
            if idx not in self.axs_twin_x:
                self.axs_twin_x[idx] = ax.twinx()
            return self.axs_twin_x[idx]

        if twin_y:
            if idx not in self.axs_twin_y:
                self.axs_twin_y[idx] = ax.twiny()
            return self.axs_twin_y[idx]
        return ax

    def _get_ax(self, idx: int = 0, cfg: dict = None):
        cfg = {} if cfg is None else cfg
        twin_x, twin_y = False, False
        if "twin_x" in cfg:
            twin_x = cfg.pop("twin_x")
        if "twin_y" in cfg:
            twin_y = cfg.pop("twin_y")
        return self.get_ax(idx, twin_x, twin_y), cfg

    def ax_set(self, idx: int = 0, cfg: Optional[AxCfg] = None):
        _cfg = cfg.matplotlib if cfg is not None else {}
        ax, _cfg = self._get_ax(idx, _cfg)

        if _cfg:
            for method in _ax_method_map:
                args = _ax_method_map[method]
                args = {k: _cfg[v] for k, v in args.items() if v in _cfg}
                if args:
                    getattr(self.axs[idx], method)(**args)
            if "visible" in _cfg:
                ax.axes.get_xaxis().set_visible(_cfg["visible"])
                ax.axes.get_yaxis().set_visible(_cfg["visible"])
            if "x_log" in _cfg:
                # 注意 不同版本传入的参数不一样，basex (旧版本)或者 base
                ax.set_xscale("log", base=_cfg["x_log"])
            if "y_log" in _cfg:
                ax.set_yscale("log", base=_cfg["y_log"])
        return ax

    def _pre_handle(self, idx: int = 0, cfg: Optional[Union[PlotCfg, LegendCfg]] = None):
        _cfg = cfg.matplotlib if cfg is not None else {}
        ax, _cfg = self._get_ax(idx, _cfg)
        return ax, _arg_rename_all(_cfg)

    def plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        ax.plot(x, y, label=label, **_cfg)

    def fill_between(self, x, y1, y2=0, where: Optional[List[bool]] = None,
                     idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        #  step : {{'pre', 'post', 'mid'}} 默认为None，填充是光滑的，开启后是阶梯状填充
        ax.fill_between(x, y1, y2, where=where, label=label, **_cfg)

    def bar(self, x, y, bottom=None, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        ax.bar(x, y, bottom=bottom, label=label, **_cfg)

    def error_bar(self, x, y, x_err=0, y_err=0, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                  cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        if _cfg.get("width"):
            _cfg["elinewidth"] = _cfg.pop("width")
        if _cfg.get("facecolor"):
            _cfg["ecolor"] = _cfg.pop("facecolor")
        ax.errorbar(x, y, xerr=x_err, yerr=y_err, label=label, **_cfg)

    def pie(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
            cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        if "color" in _cfg and isinstance(_cfg["color"], list):
            _cfg["colors"] = _cfg.pop("color")
        ax.pie(y, labels=x, autopct='%1.1f%%', **_cfg)

    def stack_plot(self, x, y, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                   cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        if label is not None:
            _cfg["labels"] = label
        ax.stackplot(x, y, **_cfg)

    def scatter(self, x, y, s=None, c=None, idx: int = 0, label: Optional[str] = None,
                cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        if "color_bar" in _cfg:
            color_bar = _cfg.pop("color_bar")
        else:
            color_bar = False

        if c is not None and "color" in _cfg:
            # 保证c比color更为优先
            _cfg.pop("color")

        mappable = ax.scatter(x, y, s, c, label=label, **_cfg)

        if color_bar:
            self.fig.colorbar(mappable, ax=ax)

    def hist(self, x, bins, density=False, cumulative=False,
             idx: int = 0, label: Optional[str] = None,
             cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        _cfg = _arg_rename(_cfg, "width", "rwidth")

        ax.hist(x, bins=bins, density=density, cumulative=cumulative, label=label, **_cfg)

    def box_plot(self, x, vert=False,
                 idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        width = _cfg.get("width")
        if width is not None:
            del _cfg["width"]
        if _cfg:
            _cfg = {"patch_artist": True, "boxprops": _cfg}
        labels = [label] if (label is not None and isinstance(label, str)) else label

        ax.boxplot(x, vert=vert, labels=labels, widths=width,
                   showmeans=True, meanprops={'marker': Markers.circle.value["matplotlib"],
                                              "color": "black",
                                              "markeredgecolor": "black",
                                              "markerfacecolor": "black",
                                              },
                   medianprops={'color': 'black'}, **_cfg)

    def violin_plot(self, x, vert=False,
                    idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                    cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        width = _cfg.get("width")
        if width is not None:
            del _cfg["width"]

        # labels = [label] if (label is not None and isinstance(label, str)) else label

        parts = ax.violinplot(x, vert=vert, widths=width,
                              showmeans=False, showmedians=True)

        for pc in parts['bodies']:
            if _cfg.get("facecolor"):
                pc.set_facecolor(_cfg.get("facecolor"))
            if _cfg.get("color"):
                pc.set_edgecolor(_cfg.get("color"))
            if _cfg.get("alpha"):
                pc.set_alpha(_cfg.get("alpha"))

    def im_show(self, img, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        cmap = _cfg.get("cmap")
        alpha = _cfg.get("alpha")
        if cmap is not None:
            if "color_bar" in _cfg:
                color_bar = _cfg.pop("color_bar")
            else:
                color_bar = False
            mappable = ax.imshow(img, cmap=cmap, alpha=alpha)
            if color_bar:
                self.fig.colorbar(mappable, ax=ax)
        else:
            ax.imshow(img, alpha=alpha)

    def add_box(self, box, idx: int = 0, label: Optional[Union[str, List[str]]] = None, cfg: Optional[PlotCfg] = None):
        # box
        #   ("xyxy", 90, 160, 600, 700)
        #   ("xywh", 90, 160, 690, 860)
        ax, _cfg = self._pre_handle(idx, cfg)

        if box[0] == "xyxy":
            x, y, w, h = box[1], box[2], box[3] - box[1], box[4] - box[2]
        elif box[0] == "xywh":
            x, y, w, h = box[1], box[2], box[3], box[4]
        elif box[0] == 'center_wh':
            w, h = box[3], box[4]
            x = box[1] - 0.5 * w
            y = box[2] - 0.5 * h
        else:
            raise ValueError(box)

        facecolor = _cfg.get("facecolor")
        color = _cfg.get("color")
        width = _cfg.get("linewidth")
        fontsize = _cfg.get("fontsize")

        rec = plt.Rectangle(xy=(x, y), width=w, height=h, fill=False, edgecolor=facecolor, linewidth=width)
        ax.add_patch(rec)
        if label:
            ax.text(x, y, label,
                    va='center', ha='center', fontsize=fontsize, color=color,
                    bbox=dict(facecolor=facecolor, lw=0))

    def mask(self, x: List[Tuple[float, float]], idx: int = 0, label: Optional[Union[str, List[str]]] = None,
             cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        xs, ys = [item for item in zip(*x)]
        facecolor = _cfg.get("facecolor")
        alpha = _cfg.get("alpha")

        ax.fill(xs, ys, color=facecolor, alpha=alpha)
        if label:
            fontsize = _cfg.get("fontsize")
            color = _cfg.get("color")
            _x = sum(xs) / len(xs)
            _y = sum(ys) / len(ys)
            ax.text(_x, _y, label,
                    va='center', ha='center', fontsize=fontsize, color=color)

    def mat_show(self, mat, idx: int = 0, label: Optional[Union[str, List[str]]] = None,
                 cfg: Optional[PlotCfg] = None):
        ax, _cfg = self._pre_handle(idx, cfg)
        cmap = _cfg.get("cmap")
        mappable = ax.matshow(mat, interpolation=None, aspect='auto', cmap=cmap)

        if "fontsize" in _cfg and "fmt" in _cfg:
            fs = _cfg["fontsize"]
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    ax.text(x=j, y=i, s=_cfg["fmt"] % mat[i, j], fontsize=fs, va="center", ha='center')

        if cmap is not None:
            if "color_bar" in _cfg and _cfg["color_bar"]:
                self.fig.colorbar(mappable, ax=ax)

    def legend_set(self, idx: int = 0, cfg: Optional[LegendCfg] = None):
        if cfg is not None:
            ax, _cfg = self._pre_handle(idx, cfg)
            ax.legend(**_cfg)  # 显示图例

    def show(self):
        # self.fig.show() # 会一闪而逝
        plt.show()

    def save(self, path: str):
        self.fig.savefig(path)
