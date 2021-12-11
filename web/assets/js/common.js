/*
 * @Author: fzf404
 * @Date: 2021-10-11 14:40:04
 * @LastEditTime: 2021-10-27 18:22:09
 * @Description: 通用代码
 */

// const base_url = `api`  // mock地址
const base_url = `http://${document.domain}:8080/api`; // 后端地址

// 响应代码处理
const handle_code = (json) => {
  if (json.code != 200) {
    window.location.href = `error.html?code=${json.code}&msg=${json.msg}`;
  }
};

// 响应失败处理
const handle_fail = () => {
  window.location.href = `error.html?code=500&msg=服务器请求失败，请联系管理员!`;
};

// 隐藏加载中页面
const display = () => {
  $("#loading").hide();
  $("#load").show();
};
