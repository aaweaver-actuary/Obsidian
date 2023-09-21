import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics.gofplots import qqplot

import scipy.stats as stats
from scipy.special import comb

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

import ISLP as isl

from sklearn.datasets import (
    load_iris,
    load_breast_cancer,
    load_wine,
    load_diabetes,
    load_digits,
    load_linnerud,
)

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, Normalizer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.linear_model import LinearRegression

from itertools import combinations
from tqdm import tqdm



pio.templates.default = "ggplot2"
rcParams["figure.figsize"] = 12, 8


### my functions
class linear_regression:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def fit_vs_residual(fitted_model, trendline="lowess", title="Residuals vs. Fitted"):
        fig = px.scatter(
            x=fitted_model.fittedvalues,
            y=fitted_model.resid,
            trendline=trendline,
            title=title,
        )
        return fig

    @staticmethod
    def qq_plot(
        fitted_model,
        title="Normal Q-Q",
        line="s",
        scatter_point_color="blue",
        scatter_point_opacity=0.7,
        scatter_point_outline_color="lightblue",
        scatter_point_outline_width=0.5,
        line_color="red",
        line_dash="dash",
    ):
        std_resid = fitted_model.resid - fitted_model.resid.mean()
        std_resid /= fitted_model.resid.std()
        qq_data = qqplot(std_resid, line=line).gca().lines
        fig = go.Figure(
            data=[
                go.Scatter(
                    x=qq_data[0].get_xdata(),
                    y=qq_data[0].get_ydata(),
                    mode="markers",
                    name="Residuals",
                    # blue dots, white outline, alpha=0.7
                    marker=dict(
                        color=scatter_point_color,
                        opacity=scatter_point_opacity,
                        line=dict(
                            color=scatter_point_outline_color,
                            width=scatter_point_outline_width,
                        ),
                    ),
                ),
            ]
        )
        fig.add_trace(
            go.Scatter(
                x=qq_data[1].get_xdata(),
                y=qq_data[1].get_ydata(),
                mode="lines",
                name="Theoretical Quantiles",
                # dashed red line
                line=dict(color=line_color, dash=line_dash),
            ),
        ),
        fig.update_layout(title=title, showlegend=False)
        return fig

    @staticmethod
    def scale_location(
        fitted_model,
        title="Scale-Location",
        trendline="lowess",
        xlab="Fitted values",
        ylab="Sqrt(|standardized residuals|)",
        scatter_point_color="blue",
        scatter_point_opacity=0.7,
        scatter_point_outline_color="lightblue",
        scatter_point_outline_width=0.5,
        line_color="red",
        line_dash="dash",
    ):
        fig = px.scatter(
            x=fitted_model.fittedvalues,
            y=np.sqrt(np.abs(fitted_model.resid)),
            title=title,
            trendline=trendline,
            labels={"x": xlab, "y": ylab},
        )

        fig.update_traces(
            marker=dict(
                color=scatter_point_color,
                opacity=scatter_point_opacity,
                line=dict(
                    color=scatter_point_outline_color,
                    width=scatter_point_outline_width,
                ),
            ),
            line=dict(color=line_color, dash=line_dash),
        )

        return fig

    @staticmethod
    def residuals_vs_leverage(
        fitted_model,
        title="Residuals vs. Leverage",
        xlab="Leverage",
        ylab="Standardized Residuals",
        scatter_point_color="blue",
        scatter_point_opacity=0.7,
        scatter_point_outline_color="lightblue",
        scatter_point_outline_width=0.5,
        line_color="red",
        line_dash="dash",
    ):
        lev_plot_data = sm.graphics.plot_leverage_resid2(fitted_model).gca().lines

        fig = go.Figure(
            data=[
                go.Scatter(
                    x=lev_plot_data[0].get_xdata(),
                    y=lev_plot_data[0].get_ydata(),
                    mode="markers",
                    name="Residuals",
                    # blue dots, white outline, alpha=0.7
                    marker=dict(
                        color=scatter_point_color,
                        opacity=scatter_point_opacity,
                        line=dict(
                            color=scatter_point_outline_color,
                            width=scatter_point_outline_width,
                        ),
                    ),
                ),
            ]
        )

        fig.add_trace(
            go.Scatter(
                x=lev_plot_data[1].get_xdata(),
                y=lev_plot_data[1].get_ydata(),
                mode="lines",
                name="Cook's Distance",
                # dashed red line
                line=dict(color=line_color, dash=line_dash),
            ),
        )

        fig.update_layout(title=title, showlegend=False)

        return fig
