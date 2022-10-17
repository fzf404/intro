/*
 * @Author: fzf404
 * @Date: 2021-10-10 21:34:19
 * @LastEditTime: 2021-10-27 23:59:55
 * @Description: 自我介绍详情
 */

// 获取url参数
const url_params = new URLSearchParams(window.location.search)

// 判断是否传入id参数
if (!url_params.has('id')) {
  // 向错误处理传入错误信息
  handle_code({ code: 404, msg: '传入的学号不存在!' })
}

// 发送请求
$.get(`${base_url}/intro?id=${url_params.get('id')}`, function (json) {
  // 值验证
  if (typeof json == 'string') {
    json = JSON.parse(json)
  }

  handle_code(json)

  $('#name').text(json.data.name)
  $('#intro').text(json.data.intro)
  $('#about').text(json.data.about)

  // 0为女生，1为男生
  if (json.data.sex == '1') {
    $('#sex').text('👦')
  } else {
    $('#sex').text('👧')
  }
  // 展示页面
  display()
}).fail(
  // 错误处理
  () => handle_fail()
)
