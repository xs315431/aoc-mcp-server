import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from pydantic import Field
from typing import Annotated
from fastmcp import FastMCP

mcp = FastMCP(name="emailProxy")

AUTH_CODE = 'cxgqiyscuyxpdeac'
SENDER_EMAIL = '2830904279@qq.com'
load_dotenv()

@mcp.tool()
def send_simple_email(
    receiver_email: Annotated[str, Field(description="收件人")],
    content: Annotated[str, Field(description="邮件内容")],
    subject: Annotated[str, Field(description="邮件主题根据场合设定")]
) -> str:
    '''
    给用户指定邮箱发送内容邮件，如果用户没有提供邮箱，则需要提醒用户提供邮箱
    默认主题为“通知”，支持自定义主题。生成内容后展示给用户，用户回复确认后才进行发送。
    '''
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email
    msg['Subject'] = subject

    try:
        with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
            server.login(SENDER_EMAIL, AUTH_CODE)
            server.send_message(msg)
        return "✅ 邮件发送成功"
    except OSError as e:
        # 特别处理关闭连接时的 (-1, b'\x00\x00\x00') 错误
        if str(e) == "(-1, b'\\x00\\x00\\x00')":
            return "⚠️ 邮件已发送成功（连接关闭异常已忽略）"
        return f"❌ 邮件发送失败: {e}"
    except Exception as e:
        return f"❌ 邮件发送失败: {e}"


if __name__ == '__main__':
    # result=send_simple_email(
    #     receiver_email='2830904279@qq.com', content='中午好')
    # print(result)
    mcp.settings.port=int(os.getenv("EMAIL_PORT"))
    mcp.run('sse')
