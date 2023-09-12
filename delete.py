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

# 要删除的 IP 地址
ip_to_delete = ''  # 你想要删除的 IP 地址

# 遍历 DNS 记录，查找要删除的记录并删除它
for record in dns_records:
	if record['content'] == ip_to_delete:
		try:
			cf.zones.dns_records.delete(zone_id, record['id'])  # 删除符合条件的 DNS 记录
			print(f'DNS 记录已成功删除! IP 地址 {ip_to_delete}')
		except CloudFlare.exceptions.CloudFlareAPIError as e:
			print('删除 DNS 记录失败:', e)
			break  # 如果删除失败，可能需要采取适当的处理，此处选择退出循环