import CloudFlare

cf = CloudFlare.CloudFlare(
    email='',
    token='' # Global API key
)

zone_id = ''  # 你的域名所属的 Zone ID
ip = '' # 你需要更新的IP地址

dns_record = {
    'type': 'A',  # DNS 记录类型，可以是 'A' 或 'AAAA'（IPv6）
    'name': '',  # 域名
    'content': ip,  # IP 地址
    'proxied': False  # 是否启用代理
}

# 获取 Zone 信息
zone_info = cf.zones.get(zone_id)

# 使用适当的 Cloudflare API 端点来添加 DNS 记录
try:
    cf.zones.dns_records.post(zone_id, data=dns_record)  # 添加 DNS 记录
    print('DNS 记录已成功添加!IP地址是{}'.format(ip))
except CloudFlare.exceptions.CloudFlareAPIError as e:
    print('添加 DNS 记录失败:', e)