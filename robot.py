import asyncio
import json
import os.path
import threading
from typing import Dict, List

import aiohttp
import qqbot

from qqbot.core.util.yaml_util import YamlUtil
from qqbot.model.message import MessageEmbed, MessageEmbedField, MessageEmbedThumbnail, CreateDirectMessageRequest, \
    MessageArk, MessageArkKv, MessageArkObj, MessageArkObjKv

test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
async def _message_handler(event, message: qqbot.Message):
    """
    定义事件回调的处理
    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncMessageAPI(t_token, False)
    # 打印返回信息
    qqbot.logger.info("event %s" % event + ",receive message %s" % message.content)

    # 发送消息告知用户
    message_to_send = qqbot.MessageSendRequest(content="你好", msg_id=message.id)
    await msg_api.post_message(message.channel_id, message_to_send)


# async的异步接口的使用示例
if __name__ == "__main__":
    t_token = qqbot.Token(test_config["token"]["appid"], test_config["token"]["token"])
    # @机器人后推送被动消息
    qqbot_handler = qqbot.Handler(
        qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, _message_handler
    )
    qqbot.async_listen_events(t_token, False, qqbot_handler)
    async def get_weather(city_name: str) -> Dict:
    """
    获取天气信息
    :return: 返回天气数据的json对象
    """
    weather_api_url = "http://api.k780.com/?app=weather.today&cityNm=" + city_name + "&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json"
    async with aiohttp.ClientSession() as session:
        async with session.get(
                url=weather_api_url,
                timeout=5,
        ) as resp:
            content = await resp.text()
            content_json_obj = json.loads(content)
            return content_json_obj
