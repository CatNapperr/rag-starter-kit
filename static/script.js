async function loadUrl() {
    const urlInput = document.getElementById("url-input");
    const loadBtn = document.getElementById("load-url-btn");
    const url = urlInput.value.trim();

    if (!url) {
        alert("请输入网址！");
        return;
    }

    // 禁用按钮并显示加载中
    urlInput.disabled = true;
    loadBtn.disabled = true;
    loadBtn.textContent = "正在抓取和向量化...";

    // 在聊天框里给个提示
    appendMessage(`开始解析网页: ${url} ，请稍候...`, 'bot-msg');

    try {
        const response = await fetch('/api/load_url', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });

        if (!response.ok) {
            throw new Error('解析失败，请检查网址。');
        }

        const data = await response.json();
        appendMessage("✅ " + data.message, 'bot-msg');

    } catch (error) {
        appendMessage("❌ 解析网页失败，请检查后端报错或稍后重试。", 'bot-msg');
        console.error(error);
    } finally {
        urlInput.disabled = false;
        loadBtn.disabled = false;
        loadBtn.textContent = "解析网页";
    }
}

async function sendMessage() {
    const inputElement = document.getElementById("user-input");
    const sendButton = document.getElementById("send-btn");
    const chatBox = document.getElementById("chat-box");
    const question = inputElement.value.trim();

    if (!question) return;

    // 1. 在 UI 上显示用户的问题
    appendMessage(question, 'user-msg');
    inputElement.value = '';

    // 禁用输入和按钮，防止重复提交
    inputElement.disabled = true;
    sendButton.disabled = true;

    // 添加加载提示
    const loadingId = appendMessage('正在思考中...', 'bot-msg loading');

    try {
        // 2. 向 FastAPI 后端发送 POST 请求
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question }) // 发送的数据格式
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json(); // 接收的数据格式

        // 3. 移除加载提示，显示后端返回的真实答案
        removeMessage(loadingId);
        appendMessage(data.answer, 'bot-msg');

    } catch (error) {
        removeMessage(loadingId);
        appendMessage('抱歉，服务器出现错误或无法连接。', 'bot-msg');
        console.error('Error:', error);
    } finally {
        // 恢复输入框和按钮
        inputElement.disabled = false;
        sendButton.disabled = false;
        inputElement.focus();
    }
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

// 辅助函数：在聊天框添加消息
function appendMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    const id = 'msg-' + Date.now();
    msgDiv.id = id;
    msgDiv.className = `message ${className}`;
    msgDiv.textContent = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // 滚动到最底部
    return id;
}

// 辅助函数：移除特定消息（用于移除 loading 状态）
function removeMessage(id) {
    const msgDiv = document.getElementById(id);
    if (msgDiv) {
        msgDiv.remove();
    }
}