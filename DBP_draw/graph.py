import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
 
# API 요청 
url = 'http://apis.data.go.kr/1220000/nitemtrade/getNitemtradeList'
params = {
    'serviceKey': 'zXI3e9e6GZ/T9rKBGvEIUmCO0S+ESzWF6x9NPNcgf9pDU3H1AXOFbJe6OPL8Kz0cObNGikf9hFyI/5NyPpAZBw==',
    'strtYymm': '202001',
    'endYymm': '202012',
    'cntyCd': 'US'
}
response = requests.get(url, params=params)

# XML 파싱
root = ET.fromstring(response.content)
print(response.content)

# balPayments 추출 및 확인
bal_payments = {}
for item in root.findall('.//item'):
    print(item)
    year_text = item.find('year').text
    if year_text == "총계":  # "총계"를 포함하는 아이템은 건너뜀
        continue

    year_month = year_text.replace('.', '-')
    bal_payment = int(item.find('balPayments').text)
    
    print(f"Year-Month: {year_month}, BalPayments: {bal_payment}")  # 디버깅 출력
    
    if year_month not in bal_payments:
        bal_payments[year_month] = []
    bal_payments[year_month].append(bal_payment)
    print(bal_payment)

# 월별 평균 계산
months = sorted(bal_payments.keys())
avg_bal_payments = [np.mean(bal_payments[month]) for month in months]

# 데이터 확인
print("Months:", months)
print("Average BalPayments:", avg_bal_payments)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(months, avg_bal_payments, marker='o', linestyle='-', color='b')
plt.title('Monthly Average of balPayments')
plt.xlabel('Month')
plt.ylabel('Average balPayments')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
