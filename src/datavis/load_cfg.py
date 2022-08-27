import inspect
from typing import Union, Tuple

from .config import FigCfg, AxCfg, PlotCfg, LegendCfg
from .datavis import Plot


def obj_from_cfg(cls, cfg=None):
    if isinstance(cls, type):
        if cfg:
            names = [name for name in inspect.signature(cls.__init__).parameters]  # type: ignore
            kwargs = {name: cfg[name] for name in names[1:] if name in cfg}
            return cls(**kwargs)
        else:
            return cls()
    else:
        raise TypeError(f"cls: {type(cls)}, should be <type>")


def replace_value(d, old_value, new_value):
    assert isinstance(d, dict) or isinstance(d, list), type(d)
    assert isinstance(old_value, str), type(old_value)
    if isinstance(d, dict):
        items = d.items()
    else:  # list
        items = enumerate(d)
    for k, v in items:
        if isinstance(v, dict) or isinstance(v, list):
            replace_value(v, old_value, new_value)
        elif isinstance(v, str) and v == "{{%s}}" % old_value:
            d[k] = new_value


def from_cfg(cfg, *args, **kwargs) -> Tuple[Plot, list]:
    _kwargs_ = {}
    arg_names = cfg.get("args")
    if arg_names:
        _kwargs_ = {k: v for k, v in zip(arg_names, args)}
    _kwargs_.update(kwargs)  # 使用kwargs覆盖
    kwargs = _kwargs_

    for k, v in kwargs.items():
        replace_value(cfg, k, v)

    fig_cfg = obj_from_cfg(FigCfg, cfg.get("fig_cfg"))
    ax_cfg = obj_from_cfg(AxCfg, cfg.get("ax_cfg"))
    backend = cfg["backend"]

    plot = Plot(fig_cfg=fig_cfg, ax_cfg=ax_cfg, backend=backend)

    rets = []

    if "plots" in cfg:
        for item in cfg["plots"]:
            idx = item["idx"] if item.get("idx") else 0

            if item.get("method"):
                method_name = item["method"]
                method = getattr(plot, method_name)
                data = item["data"]

                label = item.get("label")
                plot_cfg = obj_from_cfg(PlotCfg, item.get("plot_cfg"))

                if isinstance(data, dict):
                    kwargs = {
                        "idx": idx, "label": label, "cfg": plot_cfg
                    }
                    kwargs.update(data)
                    ret = method(**kwargs)
                else:
                    ret = method(*data, idx=idx, label=label, cfg=plot_cfg)

                rets.append(ret)

            if item.get("ax_cfg") is not None:
                ax_cfg = obj_from_cfg(AxCfg, item.get("ax_cfg"))
                plot.ax_set(idx=idx, cfg=ax_cfg)

            if item.get("legend_cfg") is not None:
                legend_cfg = obj_from_cfg(LegendCfg, item.get("legend_cfg"))
                plot.legend_set(idx=idx, cfg=legend_cfg)

    return plot, rets
