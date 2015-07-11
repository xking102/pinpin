#!/usr/bin/python
# -*- coding: utf-8 -*-
from module.user.InviteCode import InviteCode
from control import pinpin


def isValidInviteCode(code):
    """
    when a user try to register,
    we will check the invite code is valid and not use
    """
    rs = InviteCode.query.filter_by(code=code, isUsed=False).first()
    if rs:
        return True
    return False


def UseInviteCode(code, uid):
    """
    when a user register succ,
    we will update the invite code status to used and link the uid
    """
    rs = InviteCode.query.filter_by(code=code, isUsed=False).first()
    if rs:
        rs.isUsed = True
        rs.userid = uid
        rs.update_dt = pinpin.getCurTimestamp()
        rs.save
        return True
    return False
