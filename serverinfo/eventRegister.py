# -*- coding: utf-8 -*-
from base.BasePost import BasePost as Parent

class EventRegister(Parent):
    def __init__(self, event=None, add=False, remove=False, rb=None):
        """
            Create, modify or remove an event listener which can report server events via Event Wait.
            POST only.

            EventRegister take a default 1 parameter as explained in NXT API Documentation

            https://nxtwiki.org/wiki/The_Nxt_API#Event_Register

            REQUEST
            :param event is one of multiple server events from the following list of event names: (optional, default is all possible events)
                > Block.BLOCK_GENERATED
                > Block.BLOCK_POPPED
                > Block.BLOCK_PUSHED
                > Peer.ADD_INBOUND
                > Peer.ADDED_ACTIVE_PEER
                > Peer.BLACKLIST
                > Peer.CHANGED_ACTIVE_PEER
                > Peer.DEACTIVATE
                > Peer.NEW_PEER
                > Peer.REMOVE
                > Peer.REMOVE_INBOUND
                > Peer.UNBLACKLIST
                > Transaction.ADDED_CONFIRMED_TRANSACTIONS
                > Transaction.ADDED_UNCONFIRMED_TRANSACTIONS
                > Transaction.REJECT_PHASED_TRANSACTION
                > Transaction.RELEASE_PHASED_TRANSACTION
                > Transaction.REMOVE_UNCONFIRMED_TRANSACTIONS
            :param add is true to add events to an existing listener (O, omit if remove is true)
            :param remove is true to remove events from an existing listener (O, omit if add is true)
            :param rb : rb object ( check base/Rb.py) (WP)

            Note: To create a new event listener, omit both add and remove. To remove an existing event listener,
            set remove to true and omit event; all registered events will be removed, any outstanding Event Wait
            will be completed and the listener will be deactivated.

            Note: An event listener is automatically deactivated whenever all registered events are removed or if
            Event Wait is not called frequently enough, according to the nxt.apiEventTimeout property.
            The timeout is not precise; the removal process runs every nxt.apiEventTimeout / 2 seconds,
            so that many extra seconds may elapse before removal; the first Event Wait call should be made immediately
            after registration to avoid deactivation.

            Note: Each API user (with a unique address) can create only one event listener.
            When a new one is created, it will replace an existing one. The maximum number of unique users is
            controlled by the nxt.maxEventUsers property.

            RESPONSE
            :return registered : is true if the operation completed successfully (B)
            :return lastBlock : (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return requestProcessingTime : (N) is the API request processing time (in millisec)

            Legenda
                ° the parameter are interchangeable on
                * if you use the secretPhrase , the transaction is immediately broadcasted to network
                ** if you use the publicKey, you create an unsigned Transaction, and you need to sign and broardcast
                *** for buying
                (R) Required
                (O) Optional
                (N) Number
                (S) String
                (B) Boolean
                (A) Array
                (OB) Object
                >   Array Element
                (WP) Wrapper Meta-parameter

        """

        # Required parameters
        self._event = event
        self._add = add
        self._remove = remove
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        for a in self.event:
            self.data["event"] = a


        super(EventRegister, self).__init__(rt="eventRegister", data=self.data, rb=self.rb)

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._tevent = [None]*3
        for a in value[:3]:
            self.tevent.append(a)
        self._event = self._tevent

    @property
    def add(self):
        return self._add

    @add.setter
    def add(self, value):
        self._add = value

    @property
    def remove(self):
        return self._remove

    @remove.setter
    def remove(self, value):
        self._remove = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value


    def run(self):
        super(EventRegister, self).run()                # calls 'BasePost.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(EventRegister, self).getData(key)  # calls 'BasePost.getData()'

