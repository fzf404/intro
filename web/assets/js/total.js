/*
 * @Author: fzf404
 * @Date: 2021-10-11 20:04:18
 * @LastEditTime: 2021-10-27 22:20:53
 * @Description: 自我介绍列表
 */

$.get(`${base_url}/total`, function (json) {
  // 值验证
  if (typeof json == 'string') {
    json = JSON.parse(json)
  }

  // 判断code
  handle_code(json)

  // 遍历数据，插入信息
  for (let key in json.data) {
    $('#list').append(`<a href="intro.html?id=${key}">${json.data[key]}</a>`)
  }

  // 关闭加载中，展示内容
  display()
}).fail(
  // 错误处理
  () => handle_fail()
)
