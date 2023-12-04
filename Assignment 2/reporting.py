import sys
import pandas as pd

def print_formatted_table(dataframe):
    def print_line(length=86):
        print('|' + '-' * (length) + '|')

    header = "| {:<20} | {:<15} | {:<20} | {:<20} |".format("Function Name", "Num. of calls", "Total Time (ms)", "Average Time (ms)")
    print(header)
    print_line()

    for index, row in dataframe.iterrows():
        row_str = "| {:<20} | {:<15} | {:<20.4f} | {:<20.4f} |".format(row['Function Name'], row['Num. of calls'], row['Total Time (ms)'], row['Average Time (ms)'])
        print(row_str)

def main():
    assert len(sys.argv) == 2, "Usage: lgl_interpreter.py trace_file.log"
    col_widths = [10, 20, 10, 26]
    df = pd.read_fwf(sys.argv[1], widths=col_widths, skiprows=1,header=None, names=['id', 'function_name', 'event', 'timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    calls_count = df.groupby('function_name').size().reset_index(name='total_calls')
    total_time = df.groupby('function_name')['timestamp'].apply(lambda x: (x.max() - x.min()).total_seconds()).reset_index(name='total_time_seconds')
    result_df = pd.merge(calls_count, total_time, on='function_name')
    result_df['Average Time (ms)'] = result_df['total_time_seconds'] / result_df['total_calls']

    display_df = pd.DataFrame({
        'Function Name': result_df['function_name'],
        'Num. of calls': result_df['total_calls'],
        'Total Time (ms)': result_df['total_time_seconds'] * 1000,
        'Average Time (ms)': result_df['Average Time (ms)'] * 1000
    })

    print_formatted_table(display_df)

if __name__ == "__main__":
    main()