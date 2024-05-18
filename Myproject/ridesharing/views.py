# Import necessary modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import initializeGraph, addEdge, AStar, calculateFare
from django.shortcuts import render
from django.http import HttpResponse

mp = [(1,"Bus Stand"),(2,"Knowledge Tree"),(3,"Office Buildings"),(4,"Shamiyana"),(5,"Profs Apartment"),(6,"Jodhpur Club"),(7,"Sports Complex"),(8,"Temple"),(9,"Chemical/Material Department"),(10,"Basics Lab"),(11,"CSE Department"),(12,"Bio Department"),(13,"Chemistry Department"),(14,"Mechanical Department"),(15,"Civil Department"),(16,"Electrical Department"),(17,"Phy Department"),(18,"LHB"),(19,"SME"),(20,"Maths Department"),(21,"Snacks Shop 1"),(22,"Snacks Shop 2"),(23,"AIDE"),(24,"Main Gate"),(25,"NIFT Gate"),(26,"Y4"),(27,"Y3"),(28,"B1"),(29,"B2"),(30,"B5"),(31,"I2"),(32,"I3"),(33,"New Mess"),(34,"Old Mess"),(35,"Laundry"),(36,"Kendriya Bhandar"),(37,"Tinkering Lab"),(38,"Barber Shop"),(39,"Stationery"),(40,"Library")]

def final_Res(shortest_path):
    res = ""
    for i in shortest_path:
        res += mp[int(i)-1][1] + "->"
    res = res[:-2]  # Removed the extra "->" at the end
    return res

@csrf_exempt
def request_ride(request):
    if request.method == 'POST':
        # Parse POST data
        start = int(request.POST.get('start'))
        end = int(request.POST.get('end'))
        print(start,"output for start")
        
        # Initialize graph and edges
        nodes = initializeGraph()
        edges = []
        
        # Define edges
        # Continuing from the previous list...
        addEdge(edges, 2, 13, 1.7)    # Knowledge Tree to Chemistry Department
        addEdge(edges, 2, 33, 1.1)    # Knowledge Tree to Snacks Shop 1
        addEdge(edges, 2, 32, 1.4)    # Knowledge Tree to Stationery
        addEdge(edges, 2, 38, 1.6)    # Knowledge Tree to Barber Shop
        addEdge(edges, 2, 17, 1.8)    # Knowledge Tree to Phy Department
        addEdge(edges, 3, 25, 2.0)    # Office Buildings to NIFT Gate
        addEdge(edges, 3, 39, 1.3)    # Office Buildings to Stationery
        addEdge(edges, 4, 24, 1.5)    # Shamiyana to Bus Stand
        addEdge(edges, 4, 17, 1.7)    # Shamiyana to Phy Department
        addEdge(edges, 5, 13, 0.9)    # Profs Apartment to Chemistry Department
        addEdge(edges, 5, 18, 1.2)    # Profs Apartment to Mechanical Department
        addEdge(edges, 5, 9, 1.1)     # Profs Apartment to Chemical/Material Department
        addEdge(edges, 5, 32, 1.4)    # Profs Apartment to Stationery
        addEdge(edges, 5, 20, 1.6)    # Profs Apartment to Maths Department
        addEdge(edges, 5, 36, 1.8)    # Profs Apartment to Y3
        addEdge(edges, 5, 33, 1.5)    # Profs Apartment to Snacks Shop 1
        addEdge(edges, 6, 24, 1.9)    # Jodhpur Club to Bus Stand
        addEdge(edges, 7, 25, 1.7)    # Sports Complex to NIFT Gate
        addEdge(edges, 7, 18, 1.9)    # Sports Complex to Mechanical Department
        addEdge(edges, 7, 21, 1.1)    # Sports Complex to Stationery
        addEdge(edges, 8, 14, 1.2)    # Temple to Mechanical Department
        addEdge(edges, 8, 32, 1.5)    # Temple to Stationery
        addEdge(edges, 8, 10, 1.8)    # Temple to Basics Lab
        addEdge(edges, 9, 11, 1.3)    # Chemical/Material Department to CSE Department
        addEdge(edges, 9, 23, 1.6)    # Chemical/Material Department to Y4
        addEdge(edges, 9, 35, 1.8)    # Chemical/Material Department to Laundry
        addEdge(edges, 9, 5, 1.0)     # Chemical/Material Department to Profs Apartment
        addEdge(edges, 9, 20, 1.2)    # Chemical/Material Department to Maths Department
        addEdge(edges, 9, 1, 1.4)     # Chemical/Material Department to Bus Stand
        addEdge(edges, 9, 28, 1.7)    # Chemical/Material Department to B1
        addEdge(edges, 10, 20, 1.5)   # Basics Lab to Maths Department
        addEdge(edges, 10, 13, 1.7)   # Basics Lab to Chemistry Department
        addEdge(edges, 10, 8, 1.9)    # Basics Lab to Temple
        addEdge(edges, 11, 9, 1.5)    # CSE Department to Chemical/Material Department
        addEdge(edges, 11, 21, 1.4)   # CSE Department to Stationery
        addEdge(edges, 11, 26, 1.2)   # CSE Department to Y3
        addEdge(edges, 11, 27, 1.2)   # CSE Department to Y3
        addEdge(edges, 11, 17, 1.6)   # CSE Department to Phy Department
        addEdge(edges, 11, 16, 1.8)   # CSE Department to Electrical Department
        addEdge(edges, 13, 2, 1.7)    # Chemistry Department to Knowledge Tree
        addEdge(edges, 13, 5, 0.9)    # Chemistry Department to Profs Apartment
        addEdge(edges, 13, 35, 1.4)   # Chemistry Department to Laundry
        addEdge(edges, 13, 10, 1.6)   # Chemistry Department to Basics Lab
        addEdge(edges, 13, 24, 1.8)   # Chemistry Department to New Mess
        addEdge(edges, 14, 36, 1.1)   # Mechanical Department to Y3
        addEdge(edges, 14, 8, 1.3)    # Mechanical Department to Temple
        addEdge(edges, 14, 19, 1.5)   # Mechanical Department to SME Department
        addEdge(edges, 14, 32, 1.7)   # Mechanical Department to Stationery
        addEdge(edges, 15, 23, 1.9)   # Civil Department to Y4
        addEdge(edges, 15, 25, 2.0)   # Civil Department to NIFT Gate
        addEdge(edges, 15, 37, 1.2)   # Civil Department to Tinkering Lab
        addEdge(edges, 15, 36, 1.5)   # Civil Department to Y3
        addEdge(edges, 15, 27, 1.8)   # Civil Department to Sports Complex
        addEdge(edges, 15, 32, 1.6)   # Civil Department to Stationery
        addEdge(edges, 16, 18, 1.3)   # Electrical Department to Bio Department
        addEdge(edges, 16, 11, 1.5)   # Electrical Department to CSE Department
        addEdge(edges, 17, 4, 1.7)    # Phy Department to Shamiyana
        addEdge(edges, 17, 11, 1.6)   # Phy Department to CSE Department
        addEdge(edges, 17, 21, 1.4)   # Phy Department to Stationery
        addEdge(edges, 17, 2, 1.8)    # Phy Department to Knowledge Tree
        addEdge(edges, 18, 5, 1.2)    # Mechanical Department to Profs Apartment
        addEdge(edges, 18, 23, 1.1)   # Mechanical Department to Y4
        addEdge(edges, 18, 39, 1.3)   # Mechanical Department to Stationery
        addEdge(edges, 18, 16, 1.5)   # Mechanical Department to Electrical Department
        addEdge(edges, 18, 7, 1.7)    # Mechanical Department to Sports Complex
        addEdge(edges, 18, 38, 1.9)   # Mechanical Department to Barber Shop
        addEdge(edges, 19, 35, 1.0)   # SME Department to Laundry
        addEdge(edges, 19, 14, 1.2)   # SME Department to Mechanical Department
        addEdge(edges, 19, 40, 1.4)   # SME Department to Library
        addEdge(edges, 20, 10, 1.6)   # Maths Department to Basics Lab
        addEdge(edges, 20, 40, 1.8)   # Maths Department to Library
        addEdge(edges, 20, 9, 1.3)    # Maths Department to Chemical/Material Department
        addEdge(edges, 20, 5, 1.5)    # Maths Department to Profs Apartment
        addEdge(edges, 21, 11, 1.1)   # Stationery to CSE Department
        addEdge(edges, 21, 23, 1.3)   # Stationery to Y4
        addEdge(edges, 21, 25, 1.5)   # Stationery to NIFT Gate
        addEdge(edges, 21, 17, 1.7)   # Stationery to Phy Department
        addEdge(edges, 21, 27, 1.9)   # Stationery to Sports Complex
        addEdge(edges, 21, 7, 1.2)    # Stationery to Office Buildings
        addEdge(edges, 22, 12, 1.4)   # Snacks Shop 2 to Bio Department
        addEdge(edges, 23, 15, 1.6)   # Y4 to Civil Department
        addEdge(edges, 23, 21, 1.8)   # Y4 to Stationery
        addEdge(edges, 23, 9, 1.2)    # Y4 to Chemical/Material Department
        addEdge(edges, 24, 4, 1.4)    # New Mess to Shamiyana
        addEdge(edges, 24, 30, 1.6)   # New Mess to I3
        addEdge(edges, 24, 6, 1.3)    # New Mess to Jodhpur Club
        addEdge(edges, 24, 39, 1.5)   # New Mess to Stationery
        addEdge(edges, 24, 13, 1.7)   # New Mess to Chemistry Department
        addEdge(edges, 25, 7, 1.9)    # NIFT Gate to Sports Complex
        addEdge(edges, 25, 15, 1.2)   # NIFT Gate to Civil Department
        addEdge(edges, 25, 27, 1.4)   # NIFT Gate to Sports Complex
        addEdge(edges, 25, 3, 1.6)    # NIFT Gate to Office Buildings
        addEdge(edges, 25, 21, 1.8)   # NIFT Gate to Stationery
        addEdge(edges, 26, 11, 1.3)   # Y3 to CSE Department
        addEdge(edges, 26, 31, 1.5)   # Y3 to Library
        addEdge(edges, 26, 30, 1.7)   # Y3 to I3
        addEdge(edges, 26, 36, 1.9)   # Y3 to Y3
        addEdge(edges, 27, 25, 1.6)   # Sports Complex to NIFT Gate
        addEdge(edges, 27, 15, 1.8)   # Sports Complex to Civil Department
        addEdge(edges, 27, 37, 2.0)   # Sports Complex to Tinkering Lab
        addEdge(edges, 27, 21, 1.2)   # Sports Complex to Stationery
        addEdge(edges, 28, 29, 1.4)   # B1 to B2
        addEdge(edges, 28, 9, 1.6)    # B1 to Chemical/Material Department
        addEdge(edges, 29, 35, 1.8)   # B2 to Laundry
        addEdge(edges, 29, 28, 1.9)   # B2 to B1
        addEdge(edges, 30, 24, 1.3)   # I3 to Shamiyana
        addEdge(edges, 30, 26, 1.5)   # I3 to Y3
        addEdge(edges, 31, 40, 1.7)   # New Mess to Library
        addEdge(edges, 31, 39, 1.1)   # New Mess to Stationery
        addEdge(edges, 31, 26, 1.3)   # New Mess to Y3
        addEdge(edges, 31, 37, 1.5)   # New Mess to Tinkering Lab
        addEdge(edges, 32, 8, 1.8)    # Stationery to Temple
        addEdge(edges, 32, 2, 1.2)    # Stationery to Knowledge Tree
        addEdge(edges, 32, 5, 1.4)    # Stationery to Profs Apartment
        addEdge(edges, 32, 14, 1.6)   # Stationery to Mechanical Department
        addEdge(edges, 32, 15, 1.9)   # Stationery to Civil Department
        addEdge(edges, 33, 2, 1.1)    # Snacks Shop 1 to Knowledge Tree
        addEdge(edges, 33, 40, 1.3)   # Snacks Shop 1 to Library
        addEdge(edges, 33, 5, 1.5)    # Snacks Shop 1 to Profs Apartment
        addEdge(edges, 35, 29, 1.7)   # Laundry to B2
        addEdge(edges, 35, 19, 1.9)   # Laundry to SME Department
        addEdge(edges, 35, 9, 1.2)    # Laundry to Chemical/Material Department
        addEdge(edges, 35, 13, 1.4)   # Laundry to Chemistry Department
        addEdge(edges, 36, 14, 1.6)   # Y3 to Mechanical Department
        addEdge(edges, 36, 15, 1.8)   # Y3 to Civil Department
        addEdge(edges, 36, 26, 1.3)   # Y3 to Y3
        addEdge(edges, 36, 5, 1.5)    # Y3 to Profs Apartment
        addEdge(edges, 37, 15, 1.7)   # Tinkering Lab to Civil Department
        addEdge(edges, 37, 27, 1.9)   # Tinkering Lab to Sports Complex
        addEdge(edges, 37, 38, 1.1)   # Tinkering Lab to Barber Shop
        addEdge(edges, 37, 31, 1.3)   # Tinkering Lab to New Mess
        addEdge(edges, 38, 37, 1.5)   # Barber Shop to Tinkering Lab
        addEdge(edges, 38, 2, 1.7)    # Barber Shop to Knowledge Tree
        addEdge(edges, 38, 40, 1.9)   # Barber Shop to Library
        addEdge(edges, 38, 18, 1.2)   # Barber Shop to Mechanical Department
        addEdge(edges, 39, 31, 1.4)   # Stationery to New Mess
        addEdge(edges, 39, 3, 1.6)    # Stationery to Office Buildings
        addEdge(edges, 39, 39, 1.8)   # Stationery to Stationery
        addEdge(edges, 39, 18, 1.1)   # Stationery to Mechanical Department
        addEdge(edges, 39, 24, 1.3)   # Stationery to New Mess
        addEdge(edges, 40, 31, 1.5)   # Library to New Mess
        addEdge(edges, 40, 20, 1.7)   # Library to Maths Department
        addEdge(edges, 40, 40, 1.9)   # Library to Library
        addEdge(edges, 40, 33, 1.2)   # Library to Snacks Shop 1
        addEdge(edges, 40, 19, 1.4)   # Library to SME Department
        addEdge(edges, 40, 38, 1.6)   # Library to Barber Shop
    
        
        
        # Find shortest path
        shortest_path = AStar(nodes, edges, start, end)
        print(shortest_path, "this is the short")
        
        if shortest_path:
            # Calculate distance and fare
            distance = sum(edge.weight for edge in edges if edge.source in shortest_path and edge.destination in shortest_path)
            fare = calculateFare(distance)
            
            # Construct result
            result = {
                'shortestPath': final_Res(shortest_path),
                'fare': fare,
            }
            print(distance)
            print(fare)
            print(result)
        else:
            result = {
                # 'message': f"No path found between nodes {start} and {end}"
            }
            print(result)

        # Return the result as a JSON response
        return JsonResponse(result)

def home(request):
    return render(request, 'interface.html')

def ride_sharing_interface(request):
    return render(request, 'interface.html')
