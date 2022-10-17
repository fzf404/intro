/*
 * @Author: fzf404
 * @Date: 2021-10-11 20:07:24
 * @LastEditTime: 2021-10-27 18:14:31
 * @Description: 新建自我介绍
 */

// 从浏览器中读取信息
let data = window.localStorage.getItem('intro')

if (data != null) {
  // 解析为object
  data = JSON.parse(data)
  // 设置储存的输入信息
  $('form [name="id"]').val(data.id)
  $('form [name="name"]').val(data.name)
  $(`form [name="sex"][value=${data.sex}]`).attr('checked', true)
  $('form [name="intro"]').val(data.intro)
  $('form [name="about"]').val(data.about)
}

$('#submit').click(function () {
  // 转换为 object
  data = {
    id: $('form [name="id"]').val(),
    name: $('form [name="name"]').val(),
    sex: $('form [name="sex"]:checked').val(),
    intro: $('form [name="intro"]').val(),
    about: $('form [name="about"]').val()
  }

  // 存储 object
  window.localStorage.setItem('intro', JSON.stringify(data))

  // 加入密码
  data['password'] = $('form [name="password"]').val()

  $.post(
    `${base_url}/new`,
    data,

    function (json) {
      // 成功处理
      if (json.code == 200) {
        window.location.href = `intro.html?id=${data.id}`
      }

      // 错误代码处理
      handle_code(json)
    }
  ).fail(() => handle_fail())
})
