import sys
import os
import datetime as DT

header_PrefetchVersion = 0x0
header_Signature = b''
header_PrefetchManagementServiceVersion = 0x0
header_FileSize = 0x0
header_ExecutableFileName = ""
header_0WithFileNameSize58orHigher =b''
header_FullPathHashValue = 0x0

def parse_header(f):

    global header_PrefetchVersion 
    global header_Signature 
    global header_PrefetchManagementServiceVersion
    global header_FileSize 
    global header_ExecutableFileName 
    global header_0WithFileNameSize58orHigher
    global header_FullPathHashValue

    # Offset
    header_offset_PrefetchVersion = 0x0
    header_offset_Signature = 0x4
    header_offset_PrefetchManagement_Service_Version = 0x8
    header_offset_FileSize = 0xC
    header_offset_ExecutableFileName = 0x10
    header_offset_0withFileNameSize58orHigher = 0x4a
    header_offset_FullPathHashValue = 0x4c
    header_offset_0 = 0x50
    header_offset_end = 0x54

    # header 범위 0x0 ~ 0x53 read
    f.seek(0)
    header = f.read(header_offset_end)

    # parsing
    header_PrefetchVersion = int.from_bytes(header[header_offset_PrefetchVersion:header_offset_Signature], "little")
    header_Signature = header[header_offset_Signature:header_offset_PrefetchManagement_Service_Version]
    header_PrefetchManagementServiceVersion = int.from_bytes(header[header_offset_PrefetchManagement_Service_Version:header_offset_FileSize], "little")
    header_FileSize = int.from_bytes(header[header_offset_FileSize:header_offset_ExecutableFileName], "little")
    header_ExecutableFileName = header[header_offset_ExecutableFileName:header_offset_0withFileNameSize58orHigher].decode('utf-8')
    header_0WithFileNameSize58orHigher = header[header_offset_0withFileNameSize58orHigher:header_offset_FullPathHashValue]
    header_FullPathHashValue = int.from_bytes(header[header_offset_FullPathHashValue:header_offset_end], "little")

Info_FileMetricsArrayInfoOffset = 0x0
Info_NumFileMetricsArray = 0x0
Info_TraceChainsArrayInfoOffset = 0x0
Info_NumTraceChainsArray = 0x0
Info_FileNameInfoOffset = 0x0
Info_FileNameInfoSize = 0x0
Info_VolumesInfoOffset = 0x0
Info_NumVolumes = 0x0
Info_VolumesInfoSize = 0x0
Info_Unknown1 = 0x0
Info_LastLaunchTime1 = 0x0
Info_LastLaunchTime2 = 0x0
Info_LastLaunchTime3 = 0x0
Info_LastLaunchTime4 = 0x0
Info_LastLaunchTime5 = 0x0
Info_LastLaunchTime6 = 0x0
Info_LastLaunchTime7 = 0x0
Info_LastLaunchTime8 = 0x0
Info_Unknown2 = 0x0
Info_RunCount = 0x0
Info_Unknown3 = 0x0

def parse_info(f):

    global Info_FileMetricsArrayInfoOffset
    global Info_NumFileMetricsArray 
    global Info_TraceChainsArrayInfoOffset
    global Info_NumTraceChainsArray 
    global Info_FileNameInfoOffset
    global Info_FileNameInfoSize
    global Info_VolumesInfoOffset
    global Info_NumVolumes
    global Info_VolumesInfoSize 
    global Info_Unknown1 
    global Info_LastLaunchTime1
    global Info_LastLaunchTime2
    global Info_LastLaunchTime3
    global Info_LastLaunchTime4
    global Info_LastLaunchTime5
    global Info_LastLaunchTime6
    global Info_LastLaunchTime7
    global Info_LastLaunchTime8
    global Info_Unknown2 
    global Info_RunCount
    global Info_Unknown3
    
    # Offset 
    Info_offset_FileMetricsArrayInfoOffset = 0x54 - 0x54
    Info_offset_NumFileMetricsArray = 0x58 - 0x54
    Info_offset_TraceChainsArrayInfoOffset = 0x5c - 0x54
    Info_offset_NumTraceChainsArray = 0x60 - 0x54
    Info_offset_FileNameInfoOffset = 0x64 - 0x54
    Info_offset_FileNameInfoSize = 0x68 - 0x54
    Info_offset_VolumesInfoOffset = 0x6c - 0x54
    Info_offset_NumVolumes = 0x70- 0x54
    Info_offset_VolumesInfoSize = 0x74 - 0x54
    Info_offset_Unknown1 = 0x78 - 0x54
    Info_offset_LastLaunchTime1 = 0x80 - 0x54
    Info_offset_LastLaunchTime2 = 0x80 - 0x54 + 8
    Info_offset_LastLaunchTime3 = 0x80 - 0x54 + 16
    Info_offset_LastLaunchTime4 = 0x80 - 0x54 + 24
    Info_offset_LastLaunchTime5 = 0x80 - 0x54 + 32
    Info_offset_LastLaunchTime6 = 0x80 - 0x54 + 40
    Info_offset_LastLaunchTime7 = 0x80 - 0x54 + 48
    Info_offset_LastLaunchTime8 = 0x80 - 0x54 + 56
    Info_offset_Unknown2 = 0xc0 - 0x54
    Info_offset_RunCount = 0xc8 - 0x54
    Info_offset_Unknown3 = 0xcc - 0x54

    # information 범위 0x54 ~ 0xd0 read
    f.seek(0x54)
    info = f.read(Info_offset_Unknown3)

    # parse
    Info_FileMetricsArrayInfoOffset = int.from_bytes(info[Info_offset_FileMetricsArrayInfoOffset:Info_offset_NumFileMetricsArray], "little")
    Info_NumFileMetricsArray = int.from_bytes(info[Info_offset_NumFileMetricsArray:Info_offset_TraceChainsArrayInfoOffset], "little")
    Info_TraceChainsArrayInfoOffset = int.from_bytes(info[Info_offset_TraceChainsArrayInfoOffset:Info_offset_NumTraceChainsArray], "little")
    Info_NumTraceChainsArray = int.from_bytes(info[Info_offset_NumTraceChainsArray:Info_offset_FileNameInfoOffset], "little")
    Info_FileNameInfoOffset = int.from_bytes(info[Info_offset_FileNameInfoOffset:Info_offset_FileNameInfoSize], "little")
    Info_FileNameInfoSize = int.from_bytes(info[Info_offset_FileNameInfoSize:Info_offset_VolumesInfoOffset], "little")
    Info_VolumesInfoOffset = int.from_bytes(info[Info_offset_VolumesInfoOffset:Info_offset_NumVolumes], "little")
    Info_NumVolumes = int.from_bytes(info[Info_offset_NumVolumes:Info_offset_VolumesInfoSize], "little")
    Info_VolumesInfoSize = int.from_bytes(info[Info_offset_VolumesInfoSize:Info_offset_Unknown1], "little")
    Info_LastLaunchTime1 = int.from_bytes(info[Info_offset_LastLaunchTime1:Info_offset_LastLaunchTime2], "little")
    Info_LastLaunchTime2 = int.from_bytes(info[Info_offset_LastLaunchTime2:Info_offset_LastLaunchTime3], "little")
    Info_LastLaunchTime3 = int.from_bytes(info[Info_offset_LastLaunchTime3:Info_offset_LastLaunchTime4], "little")
    Info_LastLaunchTime4 = int.from_bytes(info[Info_offset_LastLaunchTime4:Info_offset_LastLaunchTime5], "little")
    Info_LastLaunchTime5 = int.from_bytes(info[Info_offset_LastLaunchTime5:Info_offset_LastLaunchTime6], "little")
    Info_LastLaunchTime6 = int.from_bytes(info[Info_offset_LastLaunchTime6:Info_offset_LastLaunchTime7], "little")
    Info_LastLaunchTime7 = int.from_bytes(info[Info_offset_LastLaunchTime7:Info_offset_LastLaunchTime8], "little")
    Info_LastLaunchTime8 = int.from_bytes(info[Info_offset_LastLaunchTime8:Info_offset_Unknown2], "little")
    Info_RunCount = int.from_bytes(info[Info_offset_RunCount:Info_offset_Unknown3], "little")

metrics_FileNameStringOffset = 0x0
metrics_FileNameStringNumberOfCharacters = 0x0
metrics_Flags = 0x0
metrics_offset_FileReference_MFTEntryIndex = 0x0
metrics_offset_FileReference_SequenceNumber = 0x0

def parse_metrics_array(f, index):

    global Info_FileMetricsArrayInfoOffset
    global metrics_FileNameStringOffset 
    global metrics_FileNameStringNumberOfCharacters
    global metrics_Flags
    global metrics_FileReference_MFTEntryIndex
    global metrics_FileReference_SequenceNumber

    # Offset
    metrics_offset_FileNameStringOffset = 0x0c
    metrics_offset_FileNameStringNumberOfCharacters = 0x10
    metrics_offset_Flags = 0x14
    metrics_offset_FileReference_MFTEntryIndex = 0x18
    metrics_offset_FileReference_SequenceNumber = 0x18+6
    metrics_offset_end = 0x20

    # metrics array read
    f.seek(Info_FileMetricsArrayInfoOffset + (index * metrics_offset_end))
    metrics_Array = f.read(metrics_offset_end)

    # parse
    metrics_FileNameStringOffset = int.from_bytes(metrics_Array[metrics_offset_FileNameStringOffset:metrics_offset_FileNameStringNumberOfCharacters], "little")
    metrics_FileNameStringNumberOfCharacters = int.from_bytes(metrics_Array[metrics_offset_FileNameStringNumberOfCharacters:metrics_offset_Flags], "little")
    metrics_Flags = int.from_bytes(metrics_Array[metrics_offset_Flags:metrics_offset_FileReference_MFTEntryIndex])
    metrics_FileReference_MFTEntryIndex = int.from_bytes(metrics_Array[metrics_offset_FileReference_MFTEntryIndex:metrics_offset_FileReference_SequenceNumber], "little")
    metrics_FileReference_SequenceNumber = int.from_bytes(metrics_Array[metrics_offset_FileReference_SequenceNumber:metrics_offset_end], "little")

    # Name
    f.seek(Info_FileNameInfoOffset + metrics_FileNameStringOffset)
    filename = f.read(metrics_FileNameStringNumberOfCharacters * 2)
    
    print("\n=====metrics_array(" + str(index) + ")======")
    print("File name string offset: " + hex(metrics_FileNameStringOffset))
    print("File name string number of characters: " + str(metrics_FileNameStringNumberOfCharacters))
    print("Flags: " + hex(metrics_Flags))
    print("File Reference(MFT Entry Index): " + hex(metrics_FileReference_MFTEntryIndex))
    print("File Reference(Sequence Number): " + hex(metrics_FileReference_SequenceNumber))
    print("File name string : " + filename.decode("utf-8"))
    
def parse_trace_chain_array(f, index):

    offset_total_block_load_count = 0x0
    offset_unknown1 = 0x4
    offset_unknown2 = 0x5
    offset_unknown3 = 0x6
    offset_end = 0x8

    f.seek(Info_TraceChainsArrayInfoOffset + (index * 0x8))
    trace_chain_array = f.read(offset_end)

    print("\n=====trace_chain_array(" + hex(Info_TraceChainsArrayInfoOffset + (index * 0x8)) + ")=====")
    print("Total_block_load_count: " + hex(int.from_bytes(trace_chain_array[metrics_FileNameStringOffset:offset_unknown1], "little")))
    print("unknown1: " + hex(int.from_bytes(trace_chain_array[offset_unknown1:offset_unknown2], "little")))
    print("unknown2: " + hex(int.from_bytes(trace_chain_array[offset_unknown2:offset_unknown3], "little")))
    print("unknown3: " + hex(int.from_bytes(trace_chain_array[offset_unknown3:offset_end], "little")))

def parse_Volume(f, index):

    global Info_VolumesInfoOffset
    
    offset_VolumeDevicePathOffset = 0x0
    offset_NumberVolumeDevicePath = 0x4
    offset_VolumeCreateTime = 0x8
    offset_VolumeSerialNumber = 0x10
    offset_FileReferencesOffset = 0x14
    offset_FileReferencesDataSize = 0x18
    offset_DirectoryStringOffset = 0x1c
    offset_NumberDirectoryStrings = 0x20
    offset_unknown1 = 0x24
    offset_CopyNumberDirectoryStrings = 0x44
    offset_Unknwon2 = 0x48
    offset_end = 0x68

    f.seek(Info_VolumesInfoOffset + (index * offset_end))
    volume = f.read(offset_end)

    directory_string_offset = int.from_bytes(volume[offset_DirectoryStringOffset:offset_NumberDirectoryStrings], "little")
    number_directory_string = int.from_bytes(volume[offset_NumberDirectoryStrings:offset_unknown1], "little")
    volume_device_path_offset = int.from_bytes(volume[:offset_NumberVolumeDevicePath], "little")
    number_volume_device_path = int.from_bytes(volume[offset_NumberVolumeDevicePath:offset_VolumeCreateTime], "little")

    f.seek(Info_VolumesInfoOffset + (index * offset_end) + volume_device_path_offset)
    volume_device_path_string = f.read(number_volume_device_path * 2).decode('utf+8')
    
    f.seek(Info_VolumesInfoOffset + (index * offset_end) + directory_string_offset)
    directory_string_size = int.from_bytes(f.read(2), "little")
    directory_string = f.read(directory_string_size * 2).decode('utf-8')

    print("\n=====Volume(" + hex(Info_VolumesInfoOffset + (index * offset_end)) + ")=====")
    print("Volume Device Path Offset: " + hex(volume_device_path_offset))
    print("Number Volume Device Path: " + hex(number_volume_device_path))
    print("Volume Create Time: " + hex(int.from_bytes(volume[offset_VolumeCreateTime:offset_VolumeSerialNumber], "little")))
    print("Volume Serial Number: " + hex(int.from_bytes(volume[offset_VolumeSerialNumber:offset_FileReferencesOffset], "little")))
    print("File References Offset: " + hex(int.from_bytes(volume[offset_FileReferencesOffset:offset_FileReferencesDataSize], "little")))
    print("File References Data Size: " + hex(int.from_bytes(volume[offset_FileReferencesDataSize:offset_DirectoryStringOffset], "little")))
    print("Directory String Offset: " + hex(directory_string_offset))
    print("Number Directory Strings: " + hex(number_directory_string))
    print("Copy Number Directory Strings: " + hex(int.from_bytes(volume[offset_CopyNumberDirectoryStrings:offset_Unknwon2], "little")))

    print("\nVolume device path string: " + volume_device_path_string)
    print("Directory string: " + directory_string)
    print("Directory string size: " + str(directory_string_size))

def print_header():
    print("\n=========header=========")
    print("Prefetch Version: " + hex(header_PrefetchVersion))
    print("Signature: " + str(header_Signature))
    print("PrefetchManagementServiceVersion: " + hex(header_PrefetchManagementServiceVersion))
    print("File Size: " + str(header_FileSize))
    print("ExecutableFileName: " + header_ExecutableFileName)
    print("0WithFileNameSize58orHigher: " + str(header_0WithFileNameSize58orHigher))
    print("FullPathHashValue: " + hex(header_FullPathHashValue))

def print_info():
    print("\n=======information=======")
    print("File Metrics Array Info Offset: " + hex(Info_FileMetricsArrayInfoOffset))
    print("Num File Metrics Array: " + hex(Info_NumFileMetricsArray))
    print("Trace chains array info Offset: " + hex(Info_TraceChainsArrayInfoOffset))
    print("Num Trace chains array: " + hex(Info_NumTraceChainsArray))
    print("File Name Info Offset: " + hex(Info_FileNameInfoOffset))
    print("File Name Info Size: " + hex(Info_FileNameInfoSize))
    print("Volumes Info Offset: " + hex(Info_VolumesInfoOffset))
    print("Num Volumnes: " + hex(Info_NumVolumes))
    print("Volunes Info Size: " + hex(Info_VolumesInfoSize))
    print("Last Launch Time1: " + hex(Info_LastLaunchTime1))
    print("Last Launch Time2: " + hex(Info_LastLaunchTime2))
    print("Last Launch Time3: " + hex(Info_LastLaunchTime3))
    print("Last Launch Time4: " + hex(Info_LastLaunchTime4))
    print("Last Launch Time5: " + hex(Info_LastLaunchTime5))
    print("Last Launch Time6: " + hex(Info_LastLaunchTime6))
    print("Last Launch Time7: " + hex(Info_LastLaunchTime7))
    print("Last Launch Time8: " + hex(Info_LastLaunchTime8))
    print("RunCount: " + str(Info_RunCount))

def print_menu():
    
    print_header()
    print_info()
    print("\n=======menu=======")
    print("1. File Metrics Array")
    print("2. Trace chains array")
    print("3. Volumes Info")
    print("4. exit")
    

def main() :
    f = open(sys.argv[1], 'rb')
    print("Load file:" + sys.argv[1] + " successfully")

    parse_header(f)
    parse_info(f)

    while True :
        print_menu()
        user_input = input(">> ")

        if user_input == "1":
            
            user_input = int(input("\nindex(max:" + str(Info_NumFileMetricsArray - 1) + ")>> "))
            
            if (user_input < Info_NumFileMetricsArray) and user_input >= 0:
                parse_metrics_array(f, user_input)
            else :
                print("invalid input")

        if user_input == "2":
            
            user_input = int(input("\nindex(max:" + str(Info_NumTraceChainsArray - 1) + ")>> "))

            if (user_input < Info_NumTraceChainsArray) and user_input >= 0:
                parse_trace_chain_array(f, user_input)
            else :
                print("invalid input")

        if user_input == "3":

            user_input = int(input("\nindex(max:" + str(Info_NumVolumes - 1) + ")>> "))
            
            if (user_input < Info_NumVolumes) and user_input >= 0:
                parse_Volume(f, user_input)
            else :
                print("invalid input")

        if user_input == "4":
            break

        os.system("pause")

    f.close()

if __name__ == "__main__":
    main()
