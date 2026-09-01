"""Deterministic mock data for the Lumina Living scenario used by every lab."""
import random

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
REGIONS = ["North","South","East","West"]
CHANNELS = ["Web","Retail","Partner"]
PRODUCTS = ["Ergo Desk","Task Chair","Acoustic Pod","Sit-Stand Riser"]

def campaign_rows(n=96, seed=42):
    """96 campaign records: 4 regions x 3 channels x 8 months, deterministic."""
    rnd = random.Random(seed)
    rows, rid = [], 0
    for region in REGIONS:
        for channel in CHANNELS:
            for mi in range(8):
                rid += 1
                base = {"Web":3500,"Retail":2200,"Partner":1600}[channel]
                growth = 1 + 0.045*mi
                regf = {"North":1.0,"South":0.86,"East":1.12,"West":0.78}[region]
                impressions = int(base*growth*regf*rnd.uniform(0.92,1.08))
                ctr = rnd.uniform(0.030,0.052)
                clicks = max(1,int(impressions*ctr))
                conv = rnd.uniform(0.028,0.075)
                orders = max(0,int(clicks*conv))
                aov = {"Ergo Desk":420,"Task Chair":260,"Acoustic Pod":1450,"Sit-Stand Riser":180}
                product = PRODUCTS[(rid-1) % len(PRODUCTS)]
                revenue = round(orders*aov[product]*rnd.uniform(0.9,1.1),2)
                cost = round(revenue*rnd.uniform(0.52,0.74),2)
                returns = max(0,int(orders*rnd.uniform(0.0,0.09)))
                target = round(revenue*rnd.uniform(0.85,1.25),2)
                rows.append([f"CMP-{rid:04d}",MONTHS[mi],region,channel,product,
                             impressions,clicks,orders,revenue,cost,returns,target])
    # deliberate anomalies for the diagnostic lab (Lab 07)
    rows[17][8] = round(rows[17][8]*3.4,2)      # revenue spike
    rows[41][10] = max(rows[41][7],1)           # return rate ~100%
    rows[63][6] = 0                             # zero clicks -> divide-by-zero test
    return rows

CAMPAIGN_HEADERS = ["Record_ID","Month","Region","Channel","Product","Impressions",
                    "Clicks","Orders","Revenue","Cost","Returns","Target_Revenue"]

VENDORS = [
    ["V-1001","Aspen Office Supplies","Furniture","Approved","2026-03-14"],
    ["V-1002","Brightline Print Services","Print","Approved","2026-01-22"],
    ["V-1003","Corvus IT Hardware","IT Equipment","Approved","2026-05-09"],
    ["V-1004","Delta Facilities Group","Facilities","Suspended","2025-11-30"],
    ["V-1005","Everline Logistics","Logistics","Approved","2026-02-18"],
    ["V-1006","Fairmont Catering","Catering","Under review","2026-04-02"],
    ["V-1007","Granite Security Services","Security","Approved","2026-06-11"],
    ["V-1008","Harbour Stationery","Stationery","Approved","2026-03-28"],
    ["V-1009","Ivory Cleaning Co","Facilities","Under review","2026-05-21"],
    ["V-1010","Juniper Software Ltd","Software","Approved","2026-07-04"],
    ["V-1011","Keystone Furniture Works","Furniture","Suspended","2025-10-15"],
    ["V-1012","Lumen Electrical","Maintenance","Approved","2026-04-19"],
]
VENDOR_HEADERS = ["Vendor_ID","Vendor_Name","Category","Status","Last_Review_Date"]

ENQUIRIES = [
    ["ENQ-001","Priya Raman","priya.raman@example.com","+65 9123 4567","Please send pricing for 40 Ergo Desks for our new office."],
    ["ENQ-002","Marcus Lim","marcus.lim@example.com","+65 9234 5678","URGENT: our delivery for order 8842 has not arrived and the office opens Monday."],
    ["ENQ-003","Sofia Alvarez","sofia.alvarez@example.com","+65 9345 6789","Do the Acoustic Pods come with a ventilation option?"],
    ["ENQ-004","Daniel Ong","daniel.ong@example.com","+65 9456 7890","We would like a quotation for 15 Task Chairs with the 5-year warranty."],
    ["ENQ-005","Aisha Rahman","aisha.rahman@example.com","+65 9567 8901","URGENT: invoice INV-2291 appears to be duplicated on our statement."],
]
ENQUIRY_HEADERS = ["Enquiry_ID","Name","Email","Tel","Message"]

REQUISITIONS = [
    ["TC01","Aspen Office Supplies",1200,"Furniture","Approve — under limit, vendor approved"],
    ["TC02","Corvus IT Hardware",4800,"IT Equipment","Route to approval — over limit"],
    ["TC03","Harbour Stationery",180,"Stationery","Approve — under limit, vendor approved"],
    ["TC04","Juniper Software Ltd",9500,"Software","Route to approval — over limit"],
    ["TC05","Delta Facilities Group",2400,"Facilities","REJECT — vendor suspended"],
    ["TC06","Everline Logistics",760,"Logistics","Approve — under limit, vendor approved"],
    ["TC07","Fairmont Catering",900,"Catering","REJECT — vendor under review"],
    ["TC08","Keystone Furniture Works",300,"Furniture","REJECT — vendor suspended"],
    ["TC09","Unknown Trading Co",500,"Furniture","REJECT — vendor not on approved list"],
    ["TC10","Granite Security Services",15000,"Security","Route to approval — over limit"],
    ["TC11","Ivory Cleaning Co",450,"Facilities","REJECT — vendor under review"],
    ["TC12","aspen office supplies",1100,"Furniture","Approve — match must be case-insensitive"],
    ["TC13","Lumen Electrical",2500,"Maintenance","Route to approval — over limit"],
]
REQUISITION_HEADERS = ["Test_Case","Vendor_Name","Amount_SGD","Category","Expected_Outcome"]
