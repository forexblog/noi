# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

help_texts = {
    'lino_noi.lib.noi.migrate.Migrator' : _("""The standard migrator for noi."""),
    'lino_noi.lib.noi.migrate.Migrator.migrate_from_1_0_1' : _("""Move Deployment and Milestone from 'tickets' to new plugin
'deploy'."""),
    'lino_noi.lib.noi.user_types.EndUser' : _("""An end user is somebody who uses our software and may report
tickets, but won't work on them."""),
    'lino_noi.lib.noi.user_types.Consultant' : _("""A consultant is somebody who may both report tickets and work
on them."""),
    'lino_noi.lib.noi.user_types.Developer' : _("""A developer is somebody who may both report tickets and work
on them."""),
    'lino_noi.lib.noi.user_types.Senior' : _("""A senior developer is a developer who is additionally
responsible for triaging tickets"""),
    'lino_noi.lib.noi.user_types.SiteAdmin' : _("""Can do everything."""),
    'lino_noi.lib.tickets.TicketDetail' : _("""Customized detail_layout for Tickets in Noi"""),
    'lino_noi.lib.users.UserDetail' : _("""Layout of User Detail in Lino Noi."""),
    'lino_noi.lib.tickets.Ticket' : _("""The Django model used to represent a ticket in Noi. Adds some fields and
methods."""),
    'lino_noi.lib.tickets.Ticket.assigned_to' : _("""The user who is working on this ticket."""),
    'lino_noi.lib.tickets.Ticket.site' : _("""The site this ticket belongs to.
You can select only sites you are subscribed to."""),
    'lino_noi.lib.tickets.TicketStates.new' : _("""Somebody reported this ticket, but there was no response yet. The
ticket needs to be triaged."""),
    'lino_noi.lib.tickets.TicketStates.talk' : _("""Some worker needs discussion with the author.  We don't yet
know exactly what to do with it."""),
    'lino_noi.lib.tickets.TicketStates.todo' : _("""The ticket is confirmed and we are working on it.
It appears in the todo list of somebody (either the assigned
worker, or our general todo list)"""),
    'lino_noi.lib.tickets.TicketStates.testing' : _("""The ticket is theoretically done, but we want to confirm this
somehow, and it is not clear who should do the next step. If
it is clear that the author should do the testing, then you
should rather set the ticket to talk. If it is clear
that you (the assignee) must test it, then leave the ticket at
todo."""),
    'lino_noi.lib.tickets.TicketStates.sleeping' : _("""Waiting for some external event. We didn't decide what to do
with it."""),
    'lino_noi.lib.tickets.TicketStates.ready' : _("""The ticket is basically done, but some detail still
needs to be done by the user (e.g. testing,
confirmation, documentation,..)"""),
    'lino_noi.lib.tickets.TicketStates.done' : _("""The ticket has been done."""),
    'lino_noi.lib.tickets.TicketStates.cancelled' : _("""It has been decided that we won't fix this ticket."""),
}
