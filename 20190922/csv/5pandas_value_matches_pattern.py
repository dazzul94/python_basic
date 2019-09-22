# Invoice Number 열의 데이터 값이 001- 로 시작하는 행을 선택하고 결과를 출력 파일에 쓴다.

#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)         
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number']\
.str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)
