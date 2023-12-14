//Maya ASCII 2024 scene
//Name: poleVector_crv.ma
//Last modified: Thu, Nov 30, 2023 11:54:34 AM
//Codeset: 1252
requires maya "2024";
requires "stereoCamera" "10.0";
requires "mtoa" "5.3.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2024";
fileInfo "version" "2024";
fileInfo "cutIdentifier" "202304191415-7fa20164c6";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19045)";
fileInfo "UUID" "4E986451-471C-5650-2C6B-E59E0A2F7F60";
createNode transform -n "poleVector_crv";
	rename -uid "EB5A5864-4BB2-1B9A-29C9-6885F421E849";
createNode nurbsCurve -n "poleVector_crvShape" -p "poleVector_crv";
	rename -uid "15F9C968-41AD-C84E-E2A8-4CB8C7964BB2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 40 0 no 3
		41 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40
		41
		-1.0937334140487123 1.25 -0.94165149252213598
		-2.343733414048712 1.25 -0.63613346306264185
		-3.593733414048712 1.25 -0.20903737088293517
		-3.593733414048712 2.5 -0.20903737088293517
		-4.843733414048712 1.25 0.21824369609387317
		-6.093733414048712 0 0.94165149252213598
		-4.843733414048712 -1.25 0.21824369609387317
		-3.593733414048712 -2.5 -0.20903737088293517
		-3.593733414048712 -1.25 -0.20903737088293517
		-2.343733414048712 -1.25 -0.63613346306264185
		-1.0937334140487123 -1.25 -0.94165149252213598
		-1.0937334140487123 -2.5 -0.63613346306264185
		-1.0937334140487123 -3.75 -0.20903737088293517
		-2.343733414048712 -3.75 -0.20903737088293517
		-1.0937334140487123 -5 0.21824369609387317
		0.15626658595128773 -6.25 0.94165149252213598
		1.4062665859512877 -5 0.21824369609387317
		2.656266585951288 -3.75 -0.20903737088293517
		1.4062665859512877 -3.75 -0.20903737088293517
		1.4062665859512877 -2.5 -0.63613346306264185
		1.4062665859512877 -1.25 -0.94165149252213598
		2.656266585951288 -1.25 -0.63613346306264185
		3.906266585951288 -1.25 -0.20903737088293517
		3.906266585951288 -2.5 -0.20903737088293517
		5.156266585951288 -1.25 0.21824369609387317
		6.406266585951288 0 0.94165149252213598
		5.156266585951288 1.25 0.21824369609387317
		3.906266585951288 2.5 -0.20903737088293517
		3.906266585951288 1.25 -0.20903737088293517
		2.656266585951288 1.25 -0.63613346306264185
		1.4062665859512877 1.25 -0.94165149252213598
		1.4062665859512877 2.5 -0.63613346306264185
		1.4062665859512877 3.75 -0.20903737088293517
		2.656266585951288 3.75 -0.20903737088293517
		1.4062665859512877 5 0.21824369609387317
		0.15626658595128773 6.25 0.94165149252213598
		-1.0937334140487123 5 0.21824369609387317
		-2.343733414048712 3.75 -0.20903737088293517
		-1.0937334140487123 3.75 -0.20903737088293517
		-1.0937334140487123 2.5 -0.63613346306264185
		-1.0937334140487123 1.25 -0.94165149252213598
		;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
	setAttr ".rtfm" 1;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :standardSurface1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -sn "mtohMotionSampleStart" -ln "mtohMotionSampleStart" -at "float";
	addAttr -ci true -sn "mtohMotionSampleEnd" -ln "mtohMotionSampleEnd" -at "float";
	addAttr -ci true -sn "mtohTextureMemoryPerTexture" -ln "mtohTextureMemoryPerTexture" 
		-dv 4096 -min 1 -max 262144 -smn 16384 -at "long";
	addAttr -ci true -sn "mtohMaximumShadowMapResolution" -ln "mtohMaximumShadowMapResolution" 
		-dv 2048 -min 32 -max 8192 -at "long";
	addAttr -ci true -sn "HdStormRendererPlugin__enableTinyPrimCulling" -ln "HdStormRendererPlugin__enableTinyPrimCulling" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdStormRendererPlugin__volumeRaymarchingStepSize" -ln "HdStormRendererPlugin__volumeRaymarchingStepSize" 
		-dv 1 -at "float";
	addAttr -ci true -sn "HdStormRendererPlugin__volumeRaymarchingStepSizeLighting" 
		-ln "HdStormRendererPlugin__volumeRaymarchingStepSizeLighting" -dv 10 -at "float";
	addAttr -ci true -sn "HdStormRendererPlugin__volumeMaxTextureMemoryPerField" -ln "HdStormRendererPlugin__volumeMaxTextureMemoryPerField" 
		-dv 128 -at "float";
	addAttr -ci true -sn "HdStormRendererPlugin__maxLights" -ln "HdStormRendererPlugin__maxLights" 
		-dv 16 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__enable_progressive_render" -ln "HdArnoldRendererPlugin__enable_progressive_render" 
		-dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__progressive_min_AA_samples" -ln "HdArnoldRendererPlugin__progressive_min_AA_samples" 
		-dv -4 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__enable_adaptive_sampling" -ln "HdArnoldRendererPlugin__enable_adaptive_sampling" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__enable_gpu_rendering" -ln "HdArnoldRendererPlugin__enable_gpu_rendering" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__interactive_target_fps" -ln "HdArnoldRendererPlugin__interactive_target_fps" 
		-dv 30 -at "float";
	addAttr -ci true -sn "HdArnoldRendererPlugin__interactive_target_fps_min" -ln "HdArnoldRendererPlugin__interactive_target_fps_min" 
		-dv 20 -at "float";
	addAttr -ci true -sn "HdArnoldRendererPlugin__interactive_fps_min" -ln "HdArnoldRendererPlugin__interactive_fps_min" 
		-dv 5 -at "float";
	addAttr -ci true -sn "HdArnoldRendererPlugin__threads" -ln "HdArnoldRendererPlugin__threads" 
		-dv -1 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__AA_samples" -ln "HdArnoldRendererPlugin__AA_samples" 
		-dv 3 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__AA_samples_max" -ln "HdArnoldRendererPlugin__AA_samples_max" 
		-dv 20 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_diffuse_samples" -ln "HdArnoldRendererPlugin__GI_diffuse_samples" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_specular_samples" -ln "HdArnoldRendererPlugin__GI_specular_samples" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_transmission_samples" -ln "HdArnoldRendererPlugin__GI_transmission_samples" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_sss_samples" -ln "HdArnoldRendererPlugin__GI_sss_samples" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_volume_samples" -ln "HdArnoldRendererPlugin__GI_volume_samples" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__auto_transparency_depth" -ln "HdArnoldRendererPlugin__auto_transparency_depth" 
		-dv 10 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_diffuse_depth" -ln "HdArnoldRendererPlugin__GI_diffuse_depth" 
		-dv 1 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_specular_depth" -ln "HdArnoldRendererPlugin__GI_specular_depth" 
		-dv 1 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_transmission_depth" -ln "HdArnoldRendererPlugin__GI_transmission_depth" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_volume_depth" -ln "HdArnoldRendererPlugin__GI_volume_depth" 
		-at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__GI_total_depth" -ln "HdArnoldRendererPlugin__GI_total_depth" 
		-dv 10 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__abort_on_error" -ln "HdArnoldRendererPlugin__abort_on_error" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_textures" -ln "HdArnoldRendererPlugin__ignore_textures" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_shaders" -ln "HdArnoldRendererPlugin__ignore_shaders" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_atmosphere" -ln "HdArnoldRendererPlugin__ignore_atmosphere" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_lights" -ln "HdArnoldRendererPlugin__ignore_lights" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_shadows" -ln "HdArnoldRendererPlugin__ignore_shadows" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_subdivision" -ln "HdArnoldRendererPlugin__ignore_subdivision" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_displacement" -ln "HdArnoldRendererPlugin__ignore_displacement" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_bump" -ln "HdArnoldRendererPlugin__ignore_bump" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_motion" -ln "HdArnoldRendererPlugin__ignore_motion" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_motion_blur" -ln "HdArnoldRendererPlugin__ignore_motion_blur" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_dof" -ln "HdArnoldRendererPlugin__ignore_dof" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_smoothing" -ln "HdArnoldRendererPlugin__ignore_smoothing" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_sss" -ln "HdArnoldRendererPlugin__ignore_sss" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__ignore_operators" -ln "HdArnoldRendererPlugin__ignore_operators" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__log_mtohns_verbosity" -ln "HdArnoldRendererPlugin__log_mtohns_verbosity" 
		-dv 2 -at "long";
	addAttr -ci true -sn "HdArnoldRendererPlugin__log_mtohns_file" -ln "HdArnoldRendererPlugin__log_mtohns_file" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__profile_file" -ln "HdArnoldRendererPlugin__profile_file" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__texture_searchpath" -ln "HdArnoldRendererPlugin__texture_searchpath" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__plugin_searchpath" -ln "HdArnoldRendererPlugin__plugin_searchpath" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__procedural_searchpath" -ln "HdArnoldRendererPlugin__procedural_searchpath" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__osl_includepath" -ln "HdArnoldRendererPlugin__osl_includepath" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__subdiv_dicing_camera" -ln "HdArnoldRendererPlugin__subdiv_dicing_camera" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__subdiv_frustum_culling" -ln "HdArnoldRendererPlugin__subdiv_frustum_culling" 
		-min 0 -max 1 -at "bool";
	addAttr -ci true -sn "HdArnoldRendererPlugin__subdiv_frustum_padding" -ln "HdArnoldRendererPlugin__subdiv_frustum_padding" 
		-at "float";
	addAttr -ci true -sn "HdArnoldRendererPlugin__background" -ln "HdArnoldRendererPlugin__background" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__atmosphere" -ln "HdArnoldRendererPlugin__atmosphere" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__aov_shaders" -ln "HdArnoldRendererPlugin__aov_shaders" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__imager" -ln "HdArnoldRendererPlugin__imager" 
		-dt "string";
	addAttr -ci true -sn "HdArnoldRendererPlugin__texture_auto_generate_tx" -ln "HdArnoldRendererPlugin__texture_auto_generate_tx" 
		-dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "standardSurface1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
// End of poleVector_crv.ma
