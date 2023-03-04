$('.new-textarea').on('input', function () {
    // 这行是删除文本时，减高度用的
    this.style.height = 'auto';
    // 将 textarea 的高度设为文本的高度，达到自适应效果
    this.style.height = (this.scrollHeight) + 'px';
});
