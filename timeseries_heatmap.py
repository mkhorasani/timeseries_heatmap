import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import base64


def download_csv(name,df):

    csv = df.to_csv()
    base = base64.b64encode(csv.encode()).decode()
    file = (f'<a href="data:file/csv;base64,{base}" download="%s.csv">Download file</a>' % (name))

    return file


def heatmap(df):

    month_hours = {'January': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'February': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'March': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'April': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'May': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'June': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'July': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'August': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'September': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'October': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'November': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None},

    'December': {'12AM': None, '01AM': None, '02AM': None, '03AM': None, '04AM': None, '05AM': None,
            '06AM': None, '07AM': None, '08AM': None, '09AM': None, '10AM': None, '11AM': None,
            '12PM': None, '01PM': None, '02PM': None, '03PM': None, '04PM': None, '05PM': None,
            '06PM': None, '07PM': None, '08PM': None, '09PM': None, '10PM': None, '11PM': None}
    }

    for i in range(len(df)):
        month_hours[df.iloc[i][0]][df.iloc[i][1]] = df.loc[i]['Value']

    data_rows = list(month_hours.values())
    data = []

    for i in range(0,len(data_rows)):
        data.append(list(data_rows[i].values()))

    fig = px.imshow(data,
                    labels=dict(x="Hour", y="Month", color="Value"),
                    x=['12AM','01AM','02AM','03AM','04AM','05AM',
                    '06AM','07AM','08AM','09AM','10AM','11AM',
                    '12PM','01PM','02PM','03PM','04PM','05PM',
                    '06PM','07PM','08PM','09PM','10PM','11PM'],
                    y=['January','February','March','April','May','June',
                        'July','August','September','October','November','December']
                    )

    st.write(fig)

    return month_hours


if __name__ == '__main__':

    df = pd.read_csv('C:/Users/..../data.csv')

    for i in range(0,len(df)):
        while len(str(df.iloc[i][1]).replace('.0','')) < 4:
            df.iloc[i,1] = '0' + str(df.iloc[i][1]).replace('.0','')

        temp = datetime.datetime.strptime(str(df.iloc[i][0]).replace('.0','') + str(df.iloc[i][1]).replace('.0',''),'%Y%m%d%H%M')
        df.iloc[i,0] = temp.strftime('%B')
        df.iloc[i,1] = temp.strftime('%I%p')

    df = df.rename(columns={"Date": "Month", "Time": "Hour"})
    df = df.groupby(['Month','Hour'],sort=False,as_index=False).mean().round(1)

    st.title('Month vs. Hour Heatmap')
    heatmap_df = heatmap(df)
    st.title('Dataframe')
    st.dataframe(heatmap_df)
    st.markdown(download_csv('Heatmap Dataframe',pd.DataFrame(heatmap_df)),unsafe_allow_html=True)
