# MCP 服务器工具介绍

本项目连接了多个MCP服务器，提供了额外的工具和资源以扩展功能。以下是每个MCP服务器及其提供的工具的简要说明：

## 12306
- **get-current-date**: 获取当前日期（上海时区，格式为 "yyyy-MM-dd"）。
- **get-stations-code-in-city**: 通过中文城市名查询该城市所有火车站的名称及其对应的 `station_code`。
- **get-station-code-of-citys**: 通过中文城市名查询代表该城市的 `station_code`。
- **get-station-code-by-names**: 通过具体的中文车站名查询其 `station_code` 和车站名。
- **get-station-by-telecode**: 通过车站的 `station_telecode` 查询车站的详细信息。
- **get-tickets**: 查询12306余票信息。
- **get-interline-tickets**: 查询12306中转余票信息。
- **get-train-route-stations**: 查询特定列车车次在指定区间内的途径车站、到站时间、出发时间及停留时间等详细经停信息。

## emailProxy
- **send_simple_email**: 给用户指定邮箱发送内容邮件，支持自定义主题。

## map
- **maps_regeocode**: 将一个高德经纬度坐标转换为行政区划地址信息。
- **maps_geo**: 将详细的结构化地址转换为经纬度坐标。
- **maps_ip_location**: IP 定位根据用户输入的 IP 地址，定位 IP 的所在位置。
- **maps_weather**: 根据城市名称或者标准adcode查询指定城市的天气。
- **maps_bicycling_by_address**: 规划两个地点之间的自行车路线。
- **maps_bicycling_by_coordinates**: 规划两个坐标之间的自行车路线。
- **maps_direction_walking_by_address**: 规划两个地点之间的步行路线。
- **maps_direction_walking_by_coordinates**: 规划两个坐标之间的步行路线。
- **maps_direction_driving_by_address**: 规划两个地点之间的驾车路线。
- **maps_direction_driving_by_coordinates**: 规划两个坐标之间的驾车路线。
- **maps_direction_transit_integrated_by_address**: 规划两个地点之间的综合公共交通路线。
- **maps_direction_transit_integrated_by_coordinates**: 规划两个坐标之间的综合公共交通路线。
- **maps_distance**: 测量两个经纬度坐标之间的距离。
- **maps_text_search**: 关键词搜索 API 根据用户输入的关键字进行 POI 搜索。
- **maps_around_search**: 周边搜，根据用户传入关键词以及坐标location，搜索出radius半径范围的POI。
- **maps_search_detail**: 查询关键词搜或者周边搜获取到的POI ID的详细信息。

以上是本项目接入的所有MCP工具的概览。如果您有任何疑问或需要进一步的帮助，请随时联系我们。
