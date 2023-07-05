def generate(infile_path,outfile_path,querytype):

    fin = open(infile_path,'r')
    fout = open(outfile_path,'w')
    fout.write("//Autogenerated file - DO NOT EDIT\n")
    lines = fin.readlines()
    for line in lines:
        if "//Source file - EDIT and RUN Python Script" not in line:
            if "-asciidochandle" in line:
                fout.write(line.replace("asciidochandle",querytype))            
                print(line.replace("asciidochandle",querytype).replace("\n",""))
            elif "/req/edr/coords-response" in line:
                if querytype == "position":
                    fout.write(line.replace("/req/edr/coords-response","/req/edr/point-coords-response"))            
                    print(line.replace("/req/edr/coords-response","/req/edr/point-coords-response").replace("\n",""))
                elif querytype == "trajectory":
                    fout.write(line.replace("/req/edr/coords-response","/req/edr/linestring-coords-response"))            
                    print(line.replace("/req/edr/coords-response","/req/edr/linestring-coords-response").replace("\n",""))
                elif querytype == "corridor":
                    fout.write(line.replace("/req/edr/coords-response","/req/edr/linestring-coords-response"))            
                    print(line.replace("/req/edr/coords-response","/req/edr/linestring-coords-response").replace("\n",""))
                elif querytype == "area":
                    fout.write(line.replace("/req/edr/coords-response","/req/edr/polygon-coords-response"))            
                    print(line.replace("/req/edr/coords-response","/req/edr/polygon-coords-response").replace("\n",""))
                elif querytype == "cube":
                    fout.write(line.replace("/req/edr/coords-response","/req/edr/polygon-coords-response"))            
                    print(line.replace("/req/edr/coords-response","/req/edr/polygon-coords-response").replace("\n",""))
                else:
                    fout.write(line)            
                    print(line.replace("\n",""))
            else:
                fout.write(line)            
                print(line.replace("\n",""))                

    fin.close()
    fout.close()


#area
generate('./abstract_tests/collections/ATS_rc-coords-definition.adoc','./abstract_tests/collections/area/ATS_rc-coords-definition.adoc','area')
generate('./abstract_tests/collections/ATS_rc-coords-response.adoc','./abstract_tests/collections/area/ATS_rc-coords-response.adoc','area')
generate('./abstract_tests/collections/ATS_rc-z-definition.adoc','./abstract_tests/collections/area/ATS_rc-z-definition.adoc','area')
generate('./abstract_tests/collections/ATS_rc-z-response.adoc','./abstract_tests/collections/area/ATS_rc-z-response.adoc','area')
generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/area/ATS_rc-parameter-name-definition.adoc','area')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/area/ATS_rc-parameter-name-response.adoc','area')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/area/ATS_rc-crs-definition.adoc','area')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/area/ATS_rc-crs-response.adoc','area')
generate('./abstract_tests/core/ATS_rc-time-definition.adoc','./abstract_tests/core/area/ATS_rc-time-definition.adoc','area')
generate('./abstract_tests/core/ATS_rc-time-response.adoc','./abstract_tests/core/area/ATS_rc-time-response.adoc','area')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/area/ATS_rc-f-definition.adoc','area')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/area/ATS_rc-f-response.adoc','area')




#position

generate('./abstract_tests/collections/ATS_rc-coords-definition.adoc','./abstract_tests/collections/position/ATS_rc-coords-definition.adoc','position')
generate('./abstract_tests/collections/ATS_rc-coords-response.adoc','./abstract_tests/collections/position/ATS_rc-coords-response.adoc','position')
generate('./abstract_tests/collections/ATS_rc-z-definition.adoc','./abstract_tests/collections/position/ATS_rc-z-definition.adoc','position')
generate('./abstract_tests/collections/ATS_rc-z-response.adoc','./abstract_tests/collections/position/ATS_rc-z-response.adoc','position')
generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/position/ATS_rc-parameter-name-definition.adoc','position')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/position/ATS_rc-parameter-name-response.adoc','position')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/position/ATS_rc-crs-definition.adoc','position')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/position/ATS_rc-crs-response.adoc','position')
generate('./abstract_tests/core/ATS_rc-time-definition.adoc','./abstract_tests/core/position/ATS_rc-time-definition.adoc','position')
generate('./abstract_tests/core/ATS_rc-time-response.adoc','./abstract_tests/core/position/ATS_rc-time-response.adoc','position')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/position/ATS_rc-f-definition.adoc','position')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/position/ATS_rc-f-response.adoc','position')

#cube

# The coords param tests have been commented out because they are not supported by the Cube query.
# See https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues/423#issuecomment-1553144063
#generate('./abstract_tests/collections/ATS_rc-coords-definition.adoc','./abstract_tests/collections/cube/ATS_rc-coords-definition.adoc','cube')
#generate('./abstract_tests/collections/ATS_rc-coords-response.adoc','./abstract_tests/collections/cube/ATS_rc-coords-response.adoc','cube')

# See ATS_cube.adoc, we do not modify ATS_rc-cube-z-response.adoc. So there is no call to generate the associated file.
generate('./abstract_tests/collections/ATS_rc-z-definition.adoc','./abstract_tests/collections/cube/ATS_rc-z-definition.adoc','cube')

generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/cube/ATS_rc-parameter-name-definition.adoc','cube')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/cube/ATS_rc-parameter-name-response.adoc','cube')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/cube/ATS_rc-crs-definition.adoc','cube')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/cube/ATS_rc-crs-response.adoc','cube')
generate('./abstract_tests/core/ATS_rc-time-definition.adoc','./abstract_tests/core/cube/ATS_rc-time-definition.adoc','cube')
generate('./abstract_tests/core/ATS_rc-time-response.adoc','./abstract_tests/core/cube/ATS_rc-time-response.adoc','cube')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/cube/ATS_rc-f-definition.adoc','cube')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/cube/ATS_rc-f-response.adoc','cube')


#trajectory

generate('./abstract_tests/collections/ATS_rc-coords-definition.adoc','./abstract_tests/collections/trajectory/ATS_rc-coords-definition.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-coords-response.adoc','./abstract_tests/collections/trajectory/ATS_rc-coords-response.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/trajectory/ATS_rc-parameter-name-definition.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/trajectory/ATS_rc-parameter-name-response.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/trajectory/ATS_rc-crs-definition.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/trajectory/ATS_rc-crs-response.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/trajectory/ATS_rc-f-definition.adoc','trajectory')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/trajectory/ATS_rc-f-response.adoc','trajectory')

#corridor

generate('./abstract_tests/collections/ATS_rc-coords-definition.adoc','./abstract_tests/collections/corridor/ATS_rc-coords-definition.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-coords-response.adoc','./abstract_tests/collections/corridor/ATS_rc-coords-response.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/corridor/ATS_rc-parameter-name-definition.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/corridor/ATS_rc-parameter-name-response.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/corridor/ATS_rc-crs-definition.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/corridor/ATS_rc-crs-response.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/corridor/ATS_rc-f-definition.adoc','corridor')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/corridor/ATS_rc-f-response.adoc','corridor')

#locations

generate('./abstract_tests/core/ATS_rc-time-definition.adoc','./abstract_tests/core/locations/ATS_rc-time-definition.adoc','locations')
generate('./abstract_tests/core/ATS_rc-time-response.adoc','./abstract_tests/core/locations/ATS_rc-time-response.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-parameter-name-definition.adoc','./abstract_tests/collections/locations/ATS_rc-parameter-name-definition.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-parameter-name-response.adoc','./abstract_tests/collections/locations/ATS_rc-parameter-name-response.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-crs-definition.adoc','./abstract_tests/collections/locations/ATS_rc-crs-definition.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-crs-response.adoc','./abstract_tests/collections/locations/ATS_rc-crs-response.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-f-definition.adoc','./abstract_tests/collections/locations/ATS_rc-f-definition.adoc','locations')
generate('./abstract_tests/collections/ATS_rc-f-response.adoc','./abstract_tests/collections/locations/ATS_rc-f-response.adoc','locations')
