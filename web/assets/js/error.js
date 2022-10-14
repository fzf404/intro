/*
 * @Author: fzf404
 * @Date: 2021-10-10 22:16:54
 * @LastEditTime: 2022-10-14 21:57:07
 * @Description: 错误处理
 */

// 获取url参数
const url_params = new URLSearchParams(window.location.search)

// 判断是否传入id参数
if (url_params.has('msg') && url_params.has('code')) {
  // 编辑页面内容
  $('#msg').text(url_params.get('msg'))
  $('#code').text(url_params.get('code'))
}

// 3s后自动返回首页
setTimeout(() => {
  window.location.href = 'index.html'
}, 3000)
