from durable.lang import *

security_courses_list = ['nssii', 'tacs', 'fcs', 'ns1']
ai_ml_courses_list = ['sml', 'ml', 'cv', 'tdl', 'ai', 'dip', 'nlp', 'aml', 'dl']
general_sw_courses = ['fpp', 'dp', 'ir', 'toc', 'mc', 'sw', 'aag', 'mad']
systems_design_courses = ['wn', 'pn', 'ca', 'cmp', 'cn', 'os']
data_science_courses = ['bda', 'dmg', 'iia']
ui_ux_courses = ['dis', 'i2d', 'athcc', 'gdd', 'davp', 'df']
motion_graphics_courses = ['cg', 'img', '3daf', 'gpu', 'iag']
comp_bio_courses = ['iqb', 'pb', 'acb', 'imb', 'cadd', 'nb', 'abin', 'cgas', 'cm']
hardware_courses = ['dcs', 'owc', 'dvd', 'cmos', 'irob', 'ssd', 'vdf', 'msd', 'rs', 'aeld']
bio_stat_courses = ['bdmh', 'bstats', 'dsg', 'mlba']

possible_career = []


with ruleset('course'):
    @when_all(m.name == 'fcs')
    def handle_FCS(c):
        cgpa = input('Enter the Grade Point obtained in FCS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Security', 'CGPA' : cgpa})

    @when_all(m.name == 'tacs')
    def handle_TACS(c):
        cgpa = input('Enter the Grade Point obtained in TACS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Security', 'CGPA' : cgpa})

    @when_all(m.name == 'ns1')
    def handle_NS1(c):
        cgpa = input('Enter the Grade Point obtained in NS1: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Security', 'CGPA' : cgpa})

    @when_all(m.name == 'nssii')
    def handle_NSSII(c):
        cgpa = input('Enter the Grade Point obtained in NSSII: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Security', 'CGPA' : cgpa})

    @when_all(m.name == 'sml')
    def handle_SML(c):
        cgpa = input('Enter the Grade Point obtained in SML: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'ml')
    def handle_ML(c):
        cgpa = input('Enter the Grade Point obtained in ML: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})
    
    @when_all(m.name == 'cv')
    def handle_CV(c):
        cgpa = input('Enter the Grade Point obtained in CV: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'tdl')
    def handle_TDL(c):
        cgpa = input('Enter the Grade Point obtained in TDL: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'ai')
    def handle_AI(c):
        cgpa = input('Enter the Grade Point obtained in AI: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'dip')
    def handle_DIP(c):
        cgpa = input('Enter the Grade Point obtained in DIP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'nlp')
    def handle_NLP(c):
        cgpa = input('Enter the Grade Point obtained in NLP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'aml')
    def handle_AML(c):
        cgpa = input('Enter the Grade Point obtained in AML: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'dl')
    def handle_DL(c):
        cgpa = input('Enter the Grade Point obtained in DL: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'AI/ML', 'CGPA' : cgpa})

    @when_all(m.name == 'fpp')
    def handle_FPP(c):
        cgpa = input('Enter the Grade Point obtained in FPP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'dp')
    def handle_DP(c):
        cgpa = input('Enter the Grade Point obtained in DP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'ir')
    def handle_IR(c):
        cgpa = input('Enter the Grade Point obtained in IR: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'toc')
    def handle_TOC(c):
        cgpa = input('Enter the Grade Point obtained in TOC: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'mc')
    def handle_MC(c):
        cgpa = input('Enter the Grade Point obtained in MC: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'sw')
    def handle_SW(c):
        cgpa = input('Enter the Grade Point obtained in SW: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'aag')
    def handle_AAG(c):
        cgpa = input('Enter the Grade Point obtained in AAG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'mad')
    def handle_MAD(c):
        cgpa = input('Enter the Grade Point obtained in MAD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'General Software', 'CGPA' : cgpa})

    @when_all(m.name == 'wn')
    def handle_WN(c):
        cgpa = input('Enter the Grade Point obtained in WN: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'cmp')
    def handle_CMP(c):
        cgpa = input('Enter the Grade Point obtained in CMP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'pn')
    def handle_PN(c):
        cgpa = input('Enter the Grade Point obtained in PN: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'cn')
    def handle_CN(c):
        cgpa = input('Enter the Grade Point obtained in CN: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'os')
    def handle_OS(c):
        cgpa = input('Enter the Grade Point obtained in OS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'ca')
    def handle_CA(c):
        cgpa = input('Enter the Grade Point obtained in CA: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Systems Design', 'CGPA' : cgpa})

    @when_all(m.name == 'bda')
    def handle_BDA(c):
        cgpa = input('Enter the Grade Point obtained in BDA: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data_Science', 'CGPA' : cgpa})

    @when_all(m.name == 'dmg')
    def handle_DMG(c):
        cgpa = input('Enter the Grade Point obtained in DMG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data_Science', 'CGPA' : cgpa})

    @when_all(m.name == 'iia')
    def handle_IIA(c):
        cgpa = input('Enter the Grade Point obtained in IIA: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data_Science', 'CGPA' : cgpa})

    @when_all(m.name == 'dis')
    def handle_DIS(c):
        cgpa = input('Enter the Grade Point obtained in DIS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'i2d')
    def handle_I2D(c):
        cgpa = input('Enter the Grade Point obtained in I2D: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'athcc')
    def handle_ATHCC(c):
        cgpa = input('Enter the Grade Point obtained in ATHCC: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'gdd')
    def handle_GDD(c):
        cgpa = input('Enter the Grade Point obtained in GDD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'davp')
    def handle_DAVP(c):
        cgpa = input('Enter the Grade Point obtained in DAVP: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'df')
    def handle_DF(c):
        cgpa = input('Enter the Grade Point obtained in DF: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'UI/UX Design', 'CGPA' : cgpa})

    @when_all(m.name == 'cg')
    def handle_CG(c):
        cgpa = input('Enter the Grade Point obtained in CG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Motion Graphics', 'CGPA' : cgpa})

    @when_all(m.name == 'img')
    def handle_IMG(c):
        cgpa = input('Enter the Grade Point obtained in IMG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Motion Graphics', 'CGPA' : cgpa})

    @when_all(m.name == '3daf')
    def handle_3DAF(c):
        cgpa = input('Enter the Grade Point obtained in 3DAF: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Motion Graphics', 'CGPA' : cgpa})

    @when_all(m.name == 'gpu')
    def handle_GPU(c):
        cgpa = input('Enter the Grade Point obtained in GPU: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Motion Graphics', 'CGPA' : cgpa})

    @when_all(m.name == 'iag')
    def handle_IAG(c):
        cgpa = input('Enter the Grade Point obtained in IAG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Motion Graphics', 'CGPA' : cgpa})

    @when_all(m.name == 'iqb')
    def handle_IQB(c):
        cgpa = input('Enter the Grade Point obtained in IQB: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'pb')
    def handle_PB(c):
        cgpa = input('Enter the Grade Point obtained in PB: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'acb')
    def handle_ACB(c):
        cgpa = input('Enter the Grade Point obtained in ACB: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'imb')
    def handle_IMB(c):
        cgpa = input('Enter the Grade Point obtained in IMB: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'cadd')
    def handle_CADD(c):
        cgpa = input('Enter the Grade Point obtained in CADD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'nb')
    def handle_NB(c):
        cgpa = input('Enter the Grade Point obtained in NB: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'abin')
    def handle_ABIN(c):
        cgpa = input('Enter the Grade Point obtained in ABIN: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'cgas')
    def handle_CGAS(c):
        cgpa = input('Enter the Grade Point obtained in CGAS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'cm')
    def handle_CM(c):
        cgpa = input('Enter the Grade Point obtained in CM: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Computational Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'bdmh')
    def handle_BDMH(c):
        cgpa = input('Enter the Grade Point obtained in BDMH: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data Science Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'bstats')
    def handle_BStats(c):
        cgpa = input('Enter the Grade Point obtained in BStats: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data Science Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'dsg')
    def handle_DSG(c):
        cgpa = input('Enter the Grade Point obtained in DSG: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data Science Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'mlba')
    def handle_MLBA(c):
        cgpa = input('Enter the Grade Point obtained in MLBA: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Data Science Biology', 'CGPA' : cgpa})

    @when_all(m.name == 'dcs')
    def handle_DCS(c):
        cgpa = input('Enter the Grade Point obtained in DCS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'owc')
    def handle_OWC(c):
        cgpa = input('Enter the Grade Point obtained in OWC: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'dvd')
    def handle_DVD(c):
        cgpa = input('Enter the Grade Point obtained in DVD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'cmos')
    def handle_CMOS(c):
        cgpa = input('Enter the Grade Point obtained in CMOS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'irob')
    def handle_IRob(c):
        cgpa = input('Enter the Grade Point obtained in IRob: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'ssd')
    def handle_SSD(c):
        cgpa = input('Enter the Grade Point obtained in SSD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'vdf')
    def handle_VDF(c):
        cgpa = input('Enter the Grade Point obtained in VDF: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'msd')
    def handle_MSD(c):
        cgpa = input('Enter the Grade Point obtained in MSD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'rs')
    def handle_RS(c):
        cgpa = input('Enter the Grade Point obtained in RS: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})

    @when_all(m.name == 'aeld')
    def handle_AELD(c):
        cgpa = input('Enter the Grade Point obtained in AELD: ')
        c.assert_fact('field', {'name' : c.m.name, 'type' : 'Hardware', 'CGPA' : cgpa})





field_numCourses = {'Security' : 0, 'AI/ML' : 0, 'General Software' : 0, 'Systems Design' : 0, 'Computational Biology' : 0, 'Data Science Biology' : 0, 'UI/UX Design' : 0, 'Motion Graphics' : 0, 'Data_Science' : 0, 'Hardware' : 0}
field_averageCGPA = {'Security' : 0, 'AI/ML' : 0, 'General Software' : 0, 'Systems Design' : 0, 'Computational Biology' : 0, 'Data Science Biology' : 0, 'UI/UX Design' : 0, 'Motion Graphics' : 0, 'Data_Science' : 0, 'Hardware' : 0}
field_careerOption = {'Security' : 'Cyber Security', 'AI/ML' : 'AI/ML', 'General Software' : 'Software Development', 'Systems Design' : 'System Design', 'Computational Biology' : 'Computational Biology', 'Data Science Biology' : 'Data Science (Biology)', 'UI/UX Design' : 'UI/UX Design', 'Motion Graphics' : 'Animation/Motion Graphics', 'Data_Science' : 'Data Science', 'Hardware' : 'Hardware'}


def computeCGPA(new_add, field):
    x = field_numCourses[field]*field_averageCGPA[field]
    x += int(new_add)
    y = x/(field_numCourses[field]+1)
    field_averageCGPA[field] = y
    field_numCourses[field] += 1

with ruleset('field'):
    @when_all(m.type == 'Security')
    def handle_sec_field(d):
        # print("Inside handle_sec_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'AI/ML')
    def handle_ai_ml_field(d):
        # print("Inside handle_ai_ml_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'General Software')
    def handle_gen_sw_field(d):
        # print("Inside handle_gen_sw_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Systems Design')
    def handle_sys_des_field(d):
        # print("Inside handle_sys_des_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Computational Biology')
    def handle_comp_bio_field(d):
        # print("Inside handle_comp_bio_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Data Science Biology')
    def handle_ds_bio_field(d):
        # print("Inside handle_ds_bio_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'UI/UX Design')
    def handle_ui_ux_field(d):
        # print("Inside handle_ui_ux_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Motion Graphics')
    def handle_motion_graphics_field(d):
        # print("Inside handle_motion_graphics_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Data_Science')
    def handle_data_sci_field(d):
        # print("Inside handle_data_sc_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

    @when_all(m.type == 'Hardware')
    def handle_hw_field(d):
        # print("Inside handle_hw_field: ", d.m.CGPA)
        computeCGPA(d.m.CGPA, d.m.type)

with ruleset('interest'):
    @when_all(m.name == 'Cyber Security')
    def handle_cyb_sec_int(e):
        # print("Inside Cyber Security Interest")
        x = e.m.name
        if field_numCourses['Security']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})  # Ingenuity- Specifying unfeasibility

    @when_all(m.name == 'AI/ML')
    def handle_ai_ml_int(e):
        # print("Inside AI/ML Interest")
        x = e.m.name
        if field_numCourses['AI/ML']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Data Science')
    def handle_data_sci_int(e):
        # print("Inside Data Science Interest")
        x = e.m.name
        if field_numCourses['Data_Science']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Software Development')
    def handle_sde_int(e):
        # print("Inside Software Development Interest")
        x = e.m.name
        if field_numCourses['General Software']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'System Design')
    def handle_sys_des_int(e):
        # print("Inside System Design Interest")
        x = e.m.name
        if field_numCourses['Systems Design']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Computational Biology')
    def handle_comp_bio_int(e):
        # print("Inside Computational Biology Interest")
        x = e.m.name
        if field_numCourses['Computational Biology']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Data Science (Biology)')
    def handle_data_sci_bio_int(e):
        # print("Inside Data Science (Bio) Interest")
        x = e.m.name
        if field_numCourses['Data Science Biology']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'UI/UX Design')
    def handle_ui_ux_int(e):
        # print("Inside UI/UX Interest")
        x = e.m.name
        if field_numCourses['UI/UX Design']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Animation/Motion Graphics')
    def handle_mot_graphics_int(e):
        # print("Inside Animation/Motion Interest")
        x = e.m.name
        if field_numCourses['Motion Graphics']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Hardware')
    def handle_hw_int(e):
        # print("Inside Hardware Interest")
        x = e.m.name
        if field_numCourses['Hardware']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Data Structures and Algorithms')
    def handle_dsa_int(e):
        # print("Inside DSA Interest")
        x = 'Software Development (DSA)'
        if field_numCourses['General Software']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(m.name == 'Competitive Programming')
    def handle_cp_int(e):
        # print("Inside CP Interest")
        x = 'Software Development (CP)'
        if field_numCourses['General Software']>0:
            e.assert_fact('career', {'career_option' : x})    # Ingenuity
        else:
            e.assert_fact({'subject' : 'Interest', 'predicate' : x, 'object' : 'not feasible'})

    @when_all(+m.subject)
    def output(e):
        print('FACT: {0} {1} {2}'.format(e.m.subject, e.m.predicate, e.m.object))


with ruleset('career'):
    @when_all(+m.career_option)
    def output(f):
        # print('Fact: {0} {1} {2}'.format(f.m.subject, f.m.predicate, f.m.object))
        print('FACT: Career in {0}'.format(f.m.career_option))  # Ingenuity
        possible_career.append(f.m.career_option)


'''Make a courses list and check all the inputs of courses against that'''
'''Also Check interests'''


print('\nWelcome To CAREER ADVISORY System\n')

courses_done = []
possible_courses = []
possible_courses = possible_courses + security_courses_list + ai_ml_courses_list + general_sw_courses + systems_design_courses + data_science_courses + ui_ux_courses + motion_graphics_courses + comp_bio_courses + hardware_courses + bio_stat_courses

# print(len(possible_courses))

print('Enter all the courses related to Computer Science, Computational Biology, Hardware Electronics and Design that you have done: ')
print("Enter the acronyms of the courses and enter 'end' to stop entering the courses")
print()

while True:
    inp = input("Enter course ('end' to stop): ")
    if(inp == 'end'):
        break
    else:
        # Check if valid course
        if inp in possible_courses and inp not in courses_done:
            courses_done.append(inp)

# courses_done = ['tacs', 'fcs', 'ns1', 'nsii']
# courses_done = ['sml', 'ml', 'cv', 'tdl', 'ai', 'dip', 'nlp', 'aml', 'dl']
# courses_done = ['fpp', 'dp', 'ir', 'toc', 'mc', 'sw', 'aag', 'mad']
# courses_done = ['wn', 'pn', 'ca', 'cmp', 'cn', 'os']
# courses_done = ['bda', 'dmg', 'iia']
# courses_done = ['dis', 'i2d', 'athcc', 'gdd', 'davp', 'df']
# courses_done = ['cg', 'img', '3daf', 'gpu', 'iag']
# courses_done = ['iqb', 'pb', 'acb', 'imb', 'cadd', 'nb', 'abin', 'cgas', 'cm']
# courses_done = ['bdmh', 'bstats', 'dsg', 'mlba']



# print(courses_done)
print()

for c in courses_done:
    assert_fact('course', {'name' : c})

print()
# print('Security: ', field_numCourses['Security'])
# print('Security CGPA: ', field_averageCGPA['Security'])

# print()
# print('AI/ML: ', field_numCourses['AI/ML'])
# print('AI/ML CGPA: ', field_averageCGPA['AI/ML'])

# print()
# print('General Software: ', field_numCourses['General Software'])
# print('General Software CGPA: ', field_averageCGPA['General Software'])

# print()
# print('Systems Design: ', field_numCourses['Systems Design'])
# print('Systems Design CGPA: ', field_averageCGPA['Systems Design'])

# print()
# print('Computational Biology: ', field_numCourses['Computational Biology'])
# print('Computational Biology CGPA: ', field_averageCGPA['Computational Biology'])

# print()
# print('Data Science Biology: ', field_numCourses['Data Science Biology'])
# print('Data Science Biology CGPA: ', field_averageCGPA['Data Science Biology'])


# print()
# print('UI/UX Design: ', field_numCourses['UI/UX Design'])
# print('UI/UX Design CGPA: ', field_averageCGPA['UI/UX Design'])

# print()
# print('Motion Graphics: ', field_numCourses['Motion Graphics'])
# print('Motion Graphics CGPA: ', field_averageCGPA['Motion Graphics'])

# print()
# print('Data_Science: ', field_numCourses['Data_Science'])
# print('Data_Science CGPA: ', field_averageCGPA['Data_Science'])

# print()
# print('Hardware: ', field_numCourses['Hardware'])
# print('Hardware CGPA: ', field_averageCGPA['Hardware'])

print()

possible_interests = ['Cyber Security', 'AI/ML', 'Data Science', 'Software Development', 'System Design', 'Computational Biology', 'Data Science (Biology)', 'UI/UX Design', 'Animation/Motion Graphics', 'Hardware', 'Data Structures and Algorithms', 'Competitive Programming']

print('Enter your interests from the following list as a student of IIITD: ')
for i in possible_interests:
    print('\t->', i)

print("\nEnter your interests. Input 'end' to stop entering your choices.")
print()

interests_list = []
while True:
    inp = input('Enter interest: ')
    if inp == 'end':
        break
    if inp not in possible_interests:
        print('Invalid choice. Not taken as input.')
        continue
    if inp not in interests_list:       # This can be used as an ingenuity of assert_fact() removing duplicates
        interests_list.append(inp)
    # interests_list.append(inp)

# print(interests_list)
print()

for i in interests_list:
    assert_fact('interest', {'name' : i})

'''Assert Fact in career after checking in list possible_career'''
# print()
no_fields = 0
m1 = 'uninitialized'
m2 = 'uninitialized'
for f in field_numCourses.keys():
    if field_careerOption[f] in possible_career:
        continue
    if field_numCourses[f] == 0:
        continue
    no_fields += 1

# print('Number of fields:', no_fields)

if no_fields>=1:
    for f in field_numCourses.keys():
        if field_careerOption[f] in possible_career:
            continue
        if field_numCourses[f] == 0:
            continue
        if m1 == 'uninitialized':
            m1 = f
        elif field_averageCGPA[f] > field_averageCGPA[m1]:
            m1 = f

    assert_fact('career', {'career_option' : field_careerOption[m1]})

if no_fields>=2:
    for f in field_numCourses.keys():
        if field_careerOption[f] in possible_career:
            continue
        if field_numCourses[f] == 0:
            continue
        if m1 == m2:
            continue
        if m2 == 'uninitialized':
            m2 = f
        elif field_averageCGPA[f] > field_averageCGPA[m2]:
            m2 = f

    assert_fact('career', {'career_option' : field_careerOption[m2]})

if len(possible_career) == 0:
    print('No possible career options to be suggested')