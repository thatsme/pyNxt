# -*- coding: utf-8 -*-
from base.BaseGet import BaseGet as Parent

class SignTransaction(Parent):


    def __init__(self, unsignedTransactionJSON=None, unsignedTransactionBytes=None, prunableAttachmentJSON=None, secretPhrase=None, validate=False, rb=None):
        """
            SignTransaction take a default 1 parameter as explained in NXT API Documentation ( is deadLine requested or not ? )

            Class is working with GET method

            https://nxtwiki.org/wiki/The_Nxt_API#Sign_Transaction

            REQUEST
            :param unsignedTransactionJSON is the transactionJSON field of the transaction, without a signature subfield
            :param unsignedTransactionBytes is the unsignedTransactionBytes field of the transaction (optional, if unsignedTransactionJSON provided)
            :param prunableAttachmentJSON is a prunable attachment JSON object, if applicable, because unsignedTransactionBytes never includes prunable data
                            (optional if the transaction has already been broadcast and the prunable message can still be retrieved from the database)
            :param secretPhrase is the secret passphrase of the signing account
            :param validate is false to skip validation of the transaction bytes being signed (useful on nodes where the full blockchain is not downloaded)
            :param rb : rb object ( check base/Rb.py) (WP)

            RESPONSE
            :return signatureHash : (S) is a SHA-256 hash of the transaction signature, used in escrow transactions
            :return : verify (B) is true the signature is verified, false if not
            :return : transactionJSON (O) is the signed transaction JSON object
            :return : transactionBytes (S) are the signed transaction bytes
            :return : fullHash (S) is the full hash of the signed transaction
            :return : prunableAttachmentJSON (O) is the prunable attachment JSON object, if applicable, because transactionBytes never includes prunable data
            :return : transaction (S) is the transaction ID, derived from the fullHash
            :return : lastBlock (S) is the last block ID on the blockchain (applies if requireBlock is provided but not requireLastBlock)
            :return : requestProcessingTime (N) is the API request processing time (in millisec)

            Legenda :
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




        # is the block ID of a block that must be present in the blockchain during execution (optional)

        self._unsignedTransactionJSON = unsignedTransactionJSON
        self._unsignedTransactionBytes = unsignedTransactionBytes
        self._prunableAttachmentJSON = prunableAttachmentJSON
        self._secretPhrase = secretPhrase
        self._validate = validate
        self._rb = rb

        # Initialize dictionary
        self.data = {}

        ## Create data dictionary
        self.data["secretPhrase"] = self.secretPhrase
        self.data["validate"] = self.validate

        if self.unsignedTransactionJSON:
            self.data["unsignedTransactionJSON"] = self.unsignedTransactionJSON
        if self.unsignedTransactionBytes:
            self.data["unsignedTransactionBytes"] = self.unsignedTransactionBytes
        if self.prunableAttachmentJSON:
            self.data["prunableAttachmentJSON"] = self.prunableAttachmentJSON

        super(SignTransaction, self).__init__(rt = "signTransaction", data=self.data, rb=self.rb)

    @property
    def unsignedTransactionJSON(self):
        return self._unsignedTransactionJSON

    @unsignedTransactionJSON.setter
    def unsignedTransactionJSON(self, value):
        self._unsignedTransactionJSON = value

    @property
    def unsignedTransactionBytes(self):
        return self._unsignedTransactionBytes

    @unsignedTransactionBytes.setter
    def unsignedTransactionBytes(self, value):
        self._unsignedTransactionBytes = value

    @property
    def prunableAttachmentJSON(self):
        return self._prunableAttachmentJSON

    @prunableAttachmentJSON.setter
    def prunableAttachmentJSON(self, value):
        self._prunableAttachmentJSON = value

    @property
    def secretPhrase(self):
        return self._secretPhrase

    @secretPhrase.setter
    def secretPhrase(self, value):
        self._secretPhrase = value

    @property
    def validate(self):
        return self._validate

    @validate.setter
    def validate(self, value):
        self._validate = value

    @property
    def rb(self):
        return self._rb

    @rb.setter
    def rb(self, value):
        self._rb = value

    def run(self):
        """
        Run rest request
        """
        super(SignTransaction, self).run()                               # calls 'BaseGet.run()'

    def getData(self, key=None):
        """
        :param key: dictionary key, if None return the whole dictionary
        :return: dictionary of data
        """
        return super(SignTransaction, self).getData(key)                 # calls 'BaseGet.getData()'

    def phelp(self):
        print(SignTransaction.__doc__)

