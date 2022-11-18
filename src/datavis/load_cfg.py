import inspect
from typing import Tuple

from .config import FigCfg, AxCfg, PlotCfg, LegendCfg
from .datavis import Plot

import copy


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
    assert isinstance(d, dict) or isinstance(d, (list, tuple)), type(d)
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


"""
bugfix 创建多次，只有第一次绘图有效 close也没有用，但是使用多进程进行规避这个bug
后来发现时配置对象cfg的 拷贝引起的bug
   第一次修改cfg时候，已经替换了可以修改的值
   之后的修改，就找不到这些可以值了，所以修改就无效
"""


def from_cfg(cfg, **kwargs) -> Tuple[Plot, list]:
    # #深拷贝 防止对cfg的对象进行修改，导致只有第一次配置有限
    cfg = copy.deepcopy(cfg)

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

    # rets 就是调用method的返回，在进行拟合时候，会将拟合的参数返回
    return plot, rets
