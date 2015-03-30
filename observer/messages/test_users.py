import unittest
import messagesuser

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.msg = "Hello there"
        self.msg2 = "Hello again"
        self.expected_list = [self.msg, self.msg2]
        self.user = messagesuser.User()
        self.obs_user1 = messagesuser.User()
        self.obs_user2 = messagesuser.User()
        self.user.add_observer(self.obs_user1)
        self.user.add_observer(self.obs_user2)

    def test_sendmsg(self):
        self.user.post_message(self.msg)
        self.user.post_message(self.msg2)

        ## test last sent message is last in osberved messages arrays
        self.assertEqual(self.obs_user1.observed_messages[-1], self.msg2)
        self.assertEqual(self.obs_user2.observed_messages[-1], self.msg2)
        
        ## test observed messages list matches expected, test both users list.
        self.assertItemsEqual(self.obs_user2.observed_messages, self.expected_list)
        self.assertItemsEqual(self.obs_user1.observed_messages, self.obs_user2.observed_messages)

if __name__ == '__main__':
    unittest.main()


