"""

Design push notification :

Requirements
    Which sends the notification to the registered users
    Which receives an event from promotions team
    Sends notification to iOS, android or sends an email or all three



Event
    - generate_notification

Notification
    PromotionNotification


NotificationPublisher
    subscribers: Set[NotificationSubscriber] = set()
    PromotionNotificationPublisher


NotificationSubscriber
    + receive_notification()

    User




Decorator logic:

Receiver
    UserReceiver

receiver = UserReceiver()
if user.wants_ios:
    receiver = IosReceiver(receiver)
if user.wants_android:
    receiver = Android(receiver)

ReceiverDecorator
    -receiver: Receiver

    IosReceiverDecorator
    AndroidReceiverDecorator
    EmailReceiverDecorator

        






"""
