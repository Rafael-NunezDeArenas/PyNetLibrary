# Auto-generated — Civil 26 — Autodesk.Civil.Runtime

class CorridorError:
    """.NET: Autodesk.Civil.Runtime.CorridorError"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorErrorLevel:
    """.NET: Autodesk.Civil.Runtime.CorridorErrorLevel"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorLayoutModeDisplay:
    """.NET: Autodesk.Civil.Runtime.CorridorLayoutModeDisplay"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorMode:
    """.NET: Autodesk.Civil.Runtime.CorridorMode"""
    def __init__(self, *args) -> None: ...
    ...

class CorridorState(RuntimeState):
    """.NET: Autodesk.Civil.Runtime.CorridorState"""
    def __init__(self, *args) -> None: ...
    ResourceString: str
    ResourceString: str
    CurrentAssemblyElevation: float
    CurrentAssemblyOffset: float
    CurrentSubassemblyElevation: float
    CurrentSubassemblyOffset: float
    CurrentAssemblyFixedElevation: float
    CurrentAssemblyFixedOffset: float
    CurrentAssemblyOffsetIsFixed: bool
    CurrentAlignmentIsOffsetAlignment: bool
    CurrentCorridorName: str
    CurrentCorridorId: ObjectId
    CurrentAssemblyName: str
    CurrentAssemblyId: ObjectId
    CurrentSubassemblyVersion: str
    CurrentSubassemblyName: str
    CurrentSubassemblyId: ObjectId
    CurrentProfileId: ObjectId
    CurrentAlignmentId: ObjectId
    CurrentBaselineId: ObjectId
    CurrentElevation: float
    CurrentOffset: float
    CurrentStation: float
    CurrentRegionEndStation: float
    CurrentRegionStartStation: float
    Mode: CorridorMode
    LayoutModeDisplayType: CorridorLayoutModeDisplay
    Shapes: ShapeCollection
    Links: LinkCollection
    Points: PointCollection
    ParamsElevationTargetGlobal: ParamElevationTargetCollection
    ParamsOffsetTargetGlobal: ParamOffsetTargetCollection
    ParamsProfileGlobal: ParamProfileCollection
    ParamsAlignmentGlobal: ParamAlignmentCollection
    ParamsSurfaceGlobal: ParamSurfaceCollection
    ParamsPointGlobal: ParamPointCollection
    ParamsStringGlobal: ParamStringCollection
    ParamsBoolGlobal: ParamBoolCollection
    ParamsDoubleGlobal: ParamDoubleCollection
    ParamsLongGlobal: ParamLongCollection
    ParamsElevationTarget: ParamElevationTargetCollection
    ParamsOffsetTarget: ParamOffsetTargetCollection
    ParamsProfile: ParamProfileCollection
    ParamsAlignment: ParamAlignmentCollection
    ParamsSurface: ParamSurfaceCollection
    ParamsPoint: ParamPointCollection
    ParamsString: ParamStringCollection
    ParamsBool: ParamBoolCollection
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    CurrentMacroName: str
    CurrentMacroProject: str
    def IntersectAlignment(self, targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, maxDistance: float) -> IPoint: ...
    def IntersectLink(self, origin: IPoint, lookRight: bool, slope: float, linkCode: str) -> IPoint: ...
    def IntersectSurface(self, surfaceId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, slope: float, pointsRequired: int) -> list: ...
    def IsAboveSurface(self, surfaceId: ObjectId, alignmentId: ObjectId, point: IPoint, minimumAmountAbove: float) -> bool: ...
    def RecordError(self, error: CorridorError, errorLevel: CorridorErrorLevel, description: str, source: str, showInEventViewer: bool) -> None: ...
    def SampleSection(self, surfaceId: ObjectId, alignmentId: ObjectId, point1: IPoint, point2: IPoint) -> SampledSectionLinkCollection: ...
    def SetAxisOfRotationCrownPoint(self, nCrownPointIndex: int) -> None: ...
    def SetAxisOfRotationInformation(self, isPotentialPivot: bool, superElevationSlope: float, superElevationSlopeType: SuperelevationCrossSegmentType, isReversedSlope: bool) -> None: ...
    def SetAxisOfRotationSERange(self, dApplySE_StartOffset: float, dApplySE_EndOffset: float) -> None: ...
    def SoeToXyz(self, alignmentId: ObjectId, station: float, offset: float, elevation: float, X: float, Y: float, Z: float) -> None: ...
    def XyzToSoe(self, alignmentId: ObjectId, X: float, Y: float, Z: float, station: float, offset: float, elevation: float) -> None: ...

class IParam:
    """.NET: Autodesk.Civil.Runtime.IParam"""
    def __init__(self, *args) -> None: ...
    Value: object
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class Param:
    """.NET: Autodesk.Civil.Runtime.Param"""
    def __init__(self, *args) -> None: ...
    ...

class ParamAccessType:
    """.NET: Autodesk.Civil.Runtime.ParamAccessType"""
    def __init__(self, *args) -> None: ...
    ...

class ParamAlignment(ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>):
    """.NET: Autodesk.Civil.Runtime.ParamAlignment"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamAlignmentCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>):
    """.NET: Autodesk.Civil.Runtime.ParamAlignmentCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamAlignment
    Item: ParamAlignment
    Count: int

class ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: SlopeElevationTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: bool
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: int
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: float
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: str
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: Point3d
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>:
    """.NET: Autodesk.Civil.Runtime.ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >:
    """.NET: Autodesk.Civil.Runtime.ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >"""
    def __init__(self, *args) -> None: ...
    Key: str
    Value: WidthOffsetTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType

class ParamBool(ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >):
    """.NET: Autodesk.Civil.Runtime.ParamBool"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoBool
    Value: bool
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamBoolCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>):
    """.NET: Autodesk.Civil.Runtime.ParamBoolCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamBool
    Item: ParamBool
    Count: int
    def Add(self, name: str, value: bool) -> ParamBool: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamAlignment
    Item: ParamAlignment
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamBool
    Item: ParamBool
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> bool: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamDouble
    Item: ParamDouble
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> float: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamElevationTarget
    Item: ParamElevationTarget
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> SlopeElevationTarget: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamLong
    Item: ParamLong
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> int: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamOffsetTarget
    Item: ParamOffsetTarget
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> WidthOffsetTarget: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamPoint
    Item: ParamPoint
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> Point3d: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamProfile
    Item: ParamProfile
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamString
    Item: ParamString
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> str: ...

class ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>:
    """.NET: Autodesk.Civil.Runtime.ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>"""
    def __init__(self, *args) -> None: ...
    Item: ParamSurface
    Item: ParamSurface
    Count: int
    def GetEnumerator(self, ) -> IEnumerator: ...
    def GetObjectEnumerator(self, ) -> IEnumerator: ...
    def Value(self, index: str) -> ObjectId: ...

class ParamDouble(ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >):
    """.NET: Autodesk.Civil.Runtime.ParamDouble"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoDouble
    Value: float
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamDoubleCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>):
    """.NET: Autodesk.Civil.Runtime.ParamDoubleCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamDouble
    Item: ParamDouble
    Count: int
    def Add(self, name: str, value: float) -> ParamDouble: ...

class ParamElevationTarget(ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    """.NET: Autodesk.Civil.Runtime.ParamElevationTarget"""
    def __init__(self, *args) -> None: ...
    Value: SlopeElevationTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamElevationTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>):
    """.NET: Autodesk.Civil.Runtime.ParamElevationTargetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamElevationTarget
    Item: ParamElevationTarget
    Count: int

class ParamLogicalNameType:
    """.NET: Autodesk.Civil.Runtime.ParamLogicalNameType"""
    def __init__(self, *args) -> None: ...
    ...

class ParamLong(ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >):
    """.NET: Autodesk.Civil.Runtime.ParamLong"""
    def __init__(self, *args) -> None: ...
    TypeInfo: TypeInfoLong
    Value: int
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str
    def AddEnumData(self, name: str, displayName: str, value: int) -> None: ...
    def EnumCount(self, ) -> int: ...
    def GetEnumData(self, index: int, name: str, displayName: str, value: int) -> None: ...

class ParamLongCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>):
    """.NET: Autodesk.Civil.Runtime.ParamLongCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamLong
    Item: ParamLong
    Count: int
    def Add(self, name: str, value: int) -> ParamLong: ...

class ParamOffsetTarget(ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    """.NET: Autodesk.Civil.Runtime.ParamOffsetTarget"""
    def __init__(self, *args) -> None: ...
    Value: WidthOffsetTarget
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamOffsetTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>):
    """.NET: Autodesk.Civil.Runtime.ParamOffsetTargetCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamOffsetTarget
    Item: ParamOffsetTarget
    Count: int

class ParamPoint(ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >):
    """.NET: Autodesk.Civil.Runtime.ParamPoint"""
    def __init__(self, *args) -> None: ...
    Elevation: float
    Offset: float
    Station: float
    Value: Point3d
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str
    def GetPoint(self, station: float, offset: float, elevation: float) -> None: ...
    def SetPoint(self, station: float, offset: float, elevation: float) -> None: ...

class ParamPointCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>):
    """.NET: Autodesk.Civil.Runtime.ParamPointCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamPoint
    Item: ParamPoint
    Count: int
    def Add(self, name: str, value: Point3d) -> ParamPoint: ...

class ParamProfile(ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>):
    """.NET: Autodesk.Civil.Runtime.ParamProfile"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamProfileCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>):
    """.NET: Autodesk.Civil.Runtime.ParamProfileCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamProfile
    Item: ParamProfile
    Count: int

class ParamScope:
    """.NET: Autodesk.Civil.Runtime.ParamScope"""
    def __init__(self, *args) -> None: ...
    ...

class ParamString(ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >):
    """.NET: Autodesk.Civil.Runtime.ParamString"""
    def __init__(self, *args) -> None: ...
    Value: str
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamStringCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>):
    """.NET: Autodesk.Civil.Runtime.ParamStringCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamString
    Item: ParamString
    Count: int
    def Add(self, name: str, value: str) -> ParamString: ...

class ParamSurface(ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>):
    """.NET: Autodesk.Civil.Runtime.ParamSurface"""
    def __init__(self, *args) -> None: ...
    Value: ObjectId
    IsReadOnly: bool
    DisplayOrder: int
    Comment: str
    Description: str
    DisplayName: str
    Access: ParamAccessType
    Key: str

class ParamSurfaceCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>):
    """.NET: Autodesk.Civil.Runtime.ParamSurfaceCollection"""
    def __init__(self, *args) -> None: ...
    Item: ParamSurface
    Item: ParamSurface
    Count: int

class ParamType:
    """.NET: Autodesk.Civil.Runtime.ParamType"""
    def __init__(self, *args) -> None: ...
    ...

class ParamsOwnerType:
    """.NET: Autodesk.Civil.Runtime.ParamsOwnerType"""
    def __init__(self, *args) -> None: ...
    ...

class PipeNetworkState(RuntimeState):
    """.NET: Autodesk.Civil.Runtime.PipeNetworkState"""
    def __init__(self, *args) -> None: ...
    IsLayoutUpStream: bool
    IsCurrentPartBeingAdd: bool
    IsConnectingToStructure: bool
    IsBreakingPipe: bool
    LastPipeElevation: float
    IsInLayoutMode: bool
    CurrentStructureId: ObjectId
    CurrentPipeId: ObjectId
    ParamsBool: ParamBoolCollection
    ParamsDouble: ParamDoubleCollection
    ParamsLong: ParamLongCollection
    CurrentMacroName: str
    CurrentMacroProject: str
    def RuleResourceString(self, resId: str) -> str: ...
    def SetAlignmentOnPart(self, paramName: str, alignmentId: ObjectId) -> None: ...
    def SetBoolOnPart(self, paramName: str, value: bool) -> None: ...
    def SetDoubleOnCurrentPart(self, paramKey: str, value: float) -> None: ...
    def SetErrorMsgOnCurrentPart(self, paramKey: str, errorMessage: str) -> None: ...
    def SetLongOnPart(self, paramName: str, value: int) -> None: ...
    def SetPointOnPart(self, paramName: str, value: Point3d) -> None: ...
    def SetProfileOnPart(self, paramName: str, profileId: ObjectId) -> None: ...
    def SetStringOnPart(self, paramName: str, value: str) -> None: ...
    def SetSurfaceOnPart(self, paramName: str, surfaceId: ObjectId) -> None: ...

class RuntimeState(CivilWrapper<AeccDbRuntimeState>):
    """.NET: Autodesk.Civil.Runtime.RuntimeState"""
    def __init__(self, *args) -> None: ...
    CurrentMacroName: str
    CurrentMacroProject: str

class TypeInfoBool:
    """.NET: Autodesk.Civil.Runtime.TypeInfoBool"""
    def __init__(self, *args) -> None: ...
    ...

class TypeInfoDouble:
    """.NET: Autodesk.Civil.Runtime.TypeInfoDouble"""
    def __init__(self, *args) -> None: ...
    ...

class TypeInfoLong:
    """.NET: Autodesk.Civil.Runtime.TypeInfoLong"""
    def __init__(self, *args) -> None: ...
    ...
