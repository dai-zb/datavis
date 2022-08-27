from typing import Union, Optional, Tuple, List, Type
from enum import Enum
import warnings

from ..style import ColorInfo, Colors
from ..style import Info, Markers, LineStyles, Legends, ColorMaps, HistTypes, BaseEnum


class BaseCfg:
    @staticmethod
    def _cfg_to_str(x, lib_name: str):
        if isinstance(x, Info):
            return x[lib_name]
        return x

    @staticmethod
    def convert_value(value: Optional[Union[str, Info, Enum]], collections: Type[BaseEnum] = None):
        if isinstance(value, str):
            if collections is None:
                warnings.warn(f"unchecked value: {value}")
                return value
            else:
                return collections.index(value)
        elif isinstance(value, Info):
            return value
        elif isinstance(value, Enum):
            return value.value

    def set_value(self, name: str, value: Optional[Union[str, Info, Enum]], collections: Type[BaseEnum] = None):
        self.__dict__[name] = self.convert_value(value, collections)
        return self

    def to_dict(self, lib_name: str):
        d = {name: getattr(self, name) for name in self.__dict__ if not callable(getattr(self, name))}
        _d = {}
        for k, v in d.items():
            if v is not None:
                if isinstance(v, list):
                    _d[k] = [self._cfg_to_str(item, lib_name) for item in v]
                else:
                    _d[k] = self._cfg_to_str(v, lib_name)
        return _d

    def __getattr__(self, lib_name: str):
        return self.to_dict(lib_name)


class FigCfg(BaseCfg):
    def __init__(self,
                 figure_size: Optional[Tuple[float, float]] = None,
                 rows_number: Optional[int] = None,
                 columns_number: Optional[int] = None,
                 share_x_axis: Optional[bool] = None,
                 share_y_axis: Optional[bool] = None,
                 tight_layout: Optional[bool] = None,  # 解决轴坐标重叠的问题
                 h_space: Optional[float] = None,
                 w_space: Optional[float] = None,
                 ):
        """

        :param figure_size:
        :param rows_number:    将画布划分为n行
        :param columns_number:  将画布划分为n列
        :param share_x_axis:    所有subplot将使用相同的X轴刻度
        :param share_y_axis:    所有的subplot将使用相同的y轴刻度
        """
        self.figure_size = figure_size

        self.figure_rows_number = rows_number
        self.figure_columns_number = columns_number

        self.share_x_axis = share_x_axis  # 轴对齐
        self.share_y_axis = share_y_axis
        self.tight_layout = tight_layout

        self.h_space = h_space  # 各个子图的间距
        self.w_space = w_space


class AxCfg(BaseCfg):
    def __init__(self,
                 title: Optional[str] = None,
                 title_font_size: Optional[int] = None,

                 x_label: Optional[str] = None,
                 y_label: Optional[str] = None,
                 visible: Optional[bool] = None,  # 是否显示坐标轴
                 label_font_size: Optional[int] = None,
                 # x_label的字体大小
                 # y_label的字体大小

                 # x轴的显示范围
                 x_limit_left: Optional[float] = None,  # x轴下限
                 x_limit_right: Optional[float] = None,  # x轴上限
                 # y轴的显示范围
                 y_limit_bottom: Optional[float] = None,  # y轴下限
                 y_limit_top: Optional[float] = None,  # y轴上限

                 # x轴的显示
                 x_ticks: Optional[List[float]] = None,  # 显示的刻度
                 x_tick_labels: Optional[List[str]] = None,  # 对显示刻度别名（必须在上一个生效后有效）
                 x_tick_rotation: Optional[float] = None,  # 对显示内容倾斜
                 # y轴的显示
                 y_ticks: Optional[List[float]] = None,  # 显示的刻度
                 y_tick_labels: Optional[List[str]] = None,  # 对显示刻度别名（必须在上一个生效后有效）
                 y_tick_rotation: Optional[float] = None,  # 对显示内容倾斜
                 tick_font_size: Optional[int] = None,
                 # x_tick_labels的字体大小 y_tick_labels的字体大小

                 grid: Optional[Union[str, Info, Enum]] = None,

                 x_log: Optional[float] = None,
                 y_log: Optional[float] = None,
                 # x_date
                 ):
        self.title = title  # 标题
        self.title_font_size = title_font_size  # 标题的字体大小

        self.x_label = x_label  # X轴标签
        self.y_label = y_label  # Y轴标签
        self.visible = visible  # 是否显示
        self.label_font_size = label_font_size  # 标签的字体大小

        self.set_value("grid", grid, LineStyles)

        # x轴 显示范围
        self.x_limit_left = x_limit_left
        self.x_limit_right = x_limit_right
        # y轴 显示范围
        self.y_limit_bottom = y_limit_bottom
        self.y_limit_top = y_limit_top

        # x轴 坐标刻度
        self.x_ticks = x_ticks
        self.x_tick_labels = x_tick_labels
        self.x_tick_rotation = x_tick_rotation

        # y轴 显示范围 坐标刻度
        self.y_ticks = y_ticks
        self.y_tick_labels = y_tick_labels
        self.y_tick_rotation = y_tick_rotation

        self.tick_font_size = tick_font_size

        # x轴 log
        self.x_log = x_log
        # y轴 log
        self.y_log = y_log


class LegendCfg(BaseCfg):
    def __init__(self,
                 location: Optional[Union[str, Info, Enum]] = None,
                 columns_number: int = 1,

                 twin_x: Optional[bool] = None,  # 双轴 共用x轴
                 twin_y: Optional[bool] = None,  # 双轴 共用y轴
                 ):
        self.set_value("location", location, Legends)
        self.columns_number = columns_number  # number of columns

        self.twin_x = twin_x
        self.twin_y = twin_y


class PlotCfg(BaseCfg):
    def __init__(self,
                 color: Optional[Union[str, ColorInfo, Enum, List[str], List[ColorInfo], List[Enum]]] = None,
                 # plot的颜色，add_box的文字颜色, mask时文字的颜色
                 # (fill_between 填充色块的透明度)
                 # 为list的时候，适用于pie,bar，可以一次给多个块进行颜色设置
                 # violin_plot边线(外围轮廓线)的颜色
                 # scatter的颜色，但是 函数入参 c 更为优先

                 face_color: Optional[Union[str, ColorInfo, Enum]] = None,
                 # boxplot、bar的填充颜色，add_box的边框颜色
                 # fill_between 填充色块的透明度
                 # error_bar中线的颜色，即ecolor

                 alpha: Optional[float] = None,
                 # im_show图片的透明度
                 # scatter 点的透明度
                 # mask时填充色块的透明度
                 # fill_between 填充色块的透明度
                 # violin_plot 填充的透明度

                 colormap: Optional[Union[str, Info, Enum]] = None,
                 # scatter，imshow, matshow 数值映射为颜色
                 color_bar: Optional[bool] = None,  # 散点图，单色图片
                 # scatter，imshow, matshow 是否显示颜色条，在配置了colormap时候才生效

                 marker: Optional[Union[str, Info, Enum]] = None,
                 # plot 点的样式
                 # scatter 点的样式
                 marker_size: Optional[int] = None,

                 line_style: Optional[Union[str, Info, Enum]] = None,
                 # plot 线的样式
                 line_width: Optional[int] = None,
                 # plot时候，线的宽度
                 # error_bar中主体线的宽度
                 # add_box的边框线条宽度

                 hist_type: Optional[Union[str, Info, Enum]] = None,
                 # hist(直方图)的样式

                 width: Optional[float] = None,
                 # bar的宽度，boxplot的宽度
                 # error_bar中误差线的宽度，即elinewidth

                 twin_x: Optional[bool] = None,  # 双轴 共用x轴
                 twin_y: Optional[bool] = None,  # 双轴 共用y轴

                 font_size: Optional[float] = None,
                 # add_box的文字的大小、mask时文字的大小
                 # matshow的字体大小，且只有配置了 和 fmt 之后，才会开启matshow文字显示功能

                 fmt: Optional[str] = None,
                 # matshow显示的数字样式，且只有配置了 和 fmt 之后，才会开启matshow文字显示功能
                 ):
        if isinstance(color, list):
            self.color = [self.convert_value(item, Colors) for item in color]
        else:
            self.set_value("color", color, Colors)
        self.set_value("face_color", face_color, Colors)

        self.alpha = alpha
        self.set_value("colormap", colormap, ColorMaps)
        self.color_bar = color_bar

        self.set_value("marker", marker, Markers)

        self.marker_size = marker_size

        self.set_value("line_style", line_style, LineStyles)

        self.line_width = line_width

        self.set_value("hist_type", hist_type, HistTypes)

        self.width = width

        self.twin_x = twin_x
        self.twin_y = twin_y

        self.font_size = font_size

        self.fmt = fmt
