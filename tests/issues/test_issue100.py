import pandas as pd
import numpy as np

import pandas_profiling


# https://github.com/pandas-profiling/pandas-profiling/issues/100
def test_issue100():
    df = pd.DataFrame(np.random.randint(0, 1000, size=(1000, 4)), columns=list("ABCD"))
    df[["B", "C"]] = df[["B", "C"]].astype("category")

    report = df.profile_report(
        pool_size=1,
        title="Dataset with <em>Numeric</em> Categories",
        samples={"head": 20},
    )
    html = report.to_html()
    assert type(html) == str and '<p class="h2">Dataset info</p>' in html
