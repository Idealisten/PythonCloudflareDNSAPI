import CloudFlare

record_list = []

cf = CloudFlare.CloudFlare(
	email='',
	token=''  # Global API Key
)

# 域名和 Zone ID
domain_name = ''  # 你的域名
zone_id = ''  # 你的域名所属的 Zone ID

# 获取特定域名的 DNS 解析记录
dns_records = cf.zones.dns_records.get(zone_id, params={'name': domain_name})

# 打印 DNS 解析记录
for record in dns_records:
	print(record['content'])
	record_list.append(record['content'])
#   print(f"Type: {record['type']}, Name: {record['name']}, Content: {record['content']}")
