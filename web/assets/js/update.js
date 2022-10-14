/*
 * @Author: fzf404
 * @Date: 2021-10-14 16:27:31
 * @LastEditTime: 2022-10-14 21:57:20
 * @Description: 更新列表
 */

// 从浏览器中读取信息
let data = window.localStorage.getItem('intro')

if (data != null) {
  // 解析为object
  data = JSON.parse(data)
  // 写入储存的信息
  $('form [name="id"]').val(data.id)
  $('form [name="name"]').val(data.name)
  $(`form [name="sex"][value=${data.sex}]`).attr('checked', true)
  $('form [name="intro"]').val(data.intro)
  $('form [name="about"]').val(data.about)
}

$('#submit').click(function () {
  data = {
    id: $('form [name="id"]').val(),
    name: $('form [name="name"]').val(),
    sex: $('form [name="sex"]:checked').val(),
    intro: $('form [name="intro"]').val(),
    about: $('form [name="about"]').val(),
  }

  // 存储至本地
  window.localStorage.setItem('intro', JSON.stringify(data))

  // 加入密码
  data['password'] = $('form [name="password"]').val()

  // 发送 ajax 请求
  $.ajax({
    type: 'post',
    url: `${base_url}/update`,
    contentType: 'application/json',
    data: JSON.stringify(data),
    dataType: 'json',

    // 成功处理
    success: function (json) {
      // 成功处理
      if (json.code == 200) {
        window.location.href = `intro.html?id=${data.id}`
      }

      // 错误代码处理
      handle_code(json)
    },
    // 失败处理
    error: () => handle_fail(),
  })
})
