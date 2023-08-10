# rest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from hisoonni_back.utils.board import insert_utils_board

@csrf_exempt
def insert_board(request):
    if request.method == 'POST':
        # insert_utils_board 함수를 호출하여 결과를 얻음
        result = insert_utils_board()
        
        # 결과를 JSON으로 변환하여 반환
        return JsonResponse(data={"result": result}, safe=False)