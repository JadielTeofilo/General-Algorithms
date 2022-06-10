"""

7.7
 Chat Server: Explain how you would design a chat server. In particular, provide details about the
various backend components, classes, and methods. What would be the hardest problems to solve?


What is it going to be used for:
    Social media app


What is the target audience:
    All ages

What kind of messages would be sent:
    only text and emoji

Should we worry about users in general, contact lists, login and such
    only with contacts with opened messages

Should we worry about auth
    no

Should be able to see list of chats
Should be able to send a message on a chat
Should be able to create a chat

-----
Hardest problems to solve:

Storing the messages and presenting them
    The last inserted might not be in the correct order

-------



ChatServer
    user_manager
    chat_manager

ChatManager
    chats

    get_user_chats

User

UserChatMetaData
    last_seen_message: int
    user: User

Chat
    messages: List[Message] = []  # New messages appended at the end
    users: List[UserMetaData] = []

Message
    sent from
    sent at
    content
    







"""
