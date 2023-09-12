import CloudFlare

cf = CloudFlare.CloudFlare(
	email='',
	token=''
)

# 域名和 Zone ID
domain_name = ''  # 你的域名
zone_id = ''  # 你的域名所属的 Zone ID

# 获取特定域名的 DNS 解析记录
dns_records = cf.zones.dns_records.get(zone_id, params={'name': domain_name})

# 如果找到了匹配的 DNS 记录
if dns_records:
	# 假设你要更新第一个匹配的 DNS 记录
	record_to_update = dns_records[0]
	print(record_to_update['content'])
	
	# 更新 DNS 记录的 IP 地址
	updated_ip = ''  # 用你要更新的新 IP 地址替换 new_ip_address
	record_to_update['content'] = updated_ip
	
	# 使用适当的 Cloudflare API 端点来更新 DNS 记录
	try:
		cf.zones.dns_records.put(zone_id, record_to_update['id'], data=record_to_update)  # 更新 DNS 记录
		print('DNS 记录已成功更新! 新 IP 地址是 {}'.format(updated_ip))
	except CloudFlare.exceptions.CloudFlareAPIError as e:
		print('更新 DNS 记录失败:', e)
else:
	print('没有找到匹配的 DNS 记录。')