from library import app
from flask import jsonify, request, make_response
import json

from library.BLL import ScheduleSvc
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq
from library.common.Req.ScheduleReq import CreateScheduleReq, UpdateScheduleReq, SearchSchedulesReq
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.ScheduleRsp import SearchSchedulesRsp
from library.common.Rsp.SingleRsp import ErrorRsp


@app.route('/admin/schedule-management/get-schedules', methods=['POST', 'GET'])
def GetSchedules():
    req = GetItemsByPageReq(request.json)
    result = ScheduleSvc.GetScheduleByPage(req)
    res = GetItemsByPageRsp(has_prev=result['has_prev'], has_next=result['has_next'],
                            items=result['schedules']).serialize()
    return jsonify(res)


@app.route('/admin/schedule-management/create-schedule', methods=['POST', 'GET'])
def CreateSchedule():
    req = CreateScheduleReq(request.json)
    result = ScheduleSvc.CreateSchedule(req)
    return jsonify(result)


@app.route('/admin/schedule-management/update-schedule', methods=['POST', 'GET'])
def UpdateSchedule():
    req = UpdateScheduleReq(request.json)
    result = ScheduleSvc.UpdateSchedule(req)
    return jsonify(result)


@app.route('/admin/schedule-management/search-schedules', methods=['POST', 'GET'])
def SearchSchedules():
    req = SearchSchedulesReq(request.json)
    result = ScheduleSvc.SearchSchedules(req)
    res = SearchSchedulesRsp(result).serialzie()
    return jsonify(res['schedules'])
