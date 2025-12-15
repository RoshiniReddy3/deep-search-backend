from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ResearchSession
from .serializers import ResearchSessionSerializer


@api_view(['POST'])
def start_research(request):
    query = request.data.get("query")

    if not query:
        return Response(
            {"error": "query is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    research = ResearchSession.objects.create(
        title=query
    )

    serializer = ResearchSessionSerializer(research)

    return Response(
        {
            "message": "Research started (mocked)",
            "data": serializer.data
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def research_history(request):
    researches = ResearchSession.objects.all().order_by('-created_at')
    serializer = ResearchSessionSerializer(researches, many=True)

    return Response(serializer.data)
