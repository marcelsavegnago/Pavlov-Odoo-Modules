from odoo import models, fields, api

class Equipment(models.Model):
    _inherit = 'maintenance.equipment'

    customer = fields.Many2one('res.partner', string="Customer", help="The Customer/Company/Site that this equipment is located at.")
    product = fields.Many2one('product.template', string="Product", help="The product of the equipment.")
    manufacturer = fields.Many2one('res.partner', related="product.manufacturer", string="Manufacturer", help="The Manufacturer of the product (related to the selected Product)")
    image = fields.Binary(related="product.image_medium", string="Image", help="The main image which is on the product")
    role = fields.Many2one('equipment.role', string="Role", help="The role this equipment is performing.")
    parent = fields.Many2one('maintenance.equipment', string="Parent", help="Parent equipment this equipment depends on.")
    port_connected_to = fields.Many2one('equipment.phyport', string="Parent's Port")

    child_ids = fields.One2many('maintenance.equipment', 'parent', string="Child ID's", help="List of other equipment that depend on this equipment.")
    status = fields.Many2one('equipment.status', string="Status", help="Status of this equipment. (See configuration items to add/remove/change status types)")
    aka = fields.Char(string="Aka", help="If equipment has another name")
    pec = fields.Char(string="PEC", help="Product Equipment Code")
    is_spare = fields.Boolean(string="Is Spare?", help="If the equipment is marked as a spare.")
    slots = fields.One2many('equipment.slot', 'equipment', string="Slots")
    dcim_product_type = fields.Selection(related="product.dcim_product_type", string="Product Type")
    dcim_equipment = fields.Boolean(related="product.dcim_equipment", string="Is DCIM Equipment?", help="Should the product be used in the Maintenance/Equipment App")
    phyports = fields.One2many('equipment.phyport', 'equipment', string="Physical Ports")
    vports = fields.One2many('equipment.vport', 'equipment', string="Virtual Ports")
    monitoring_id = fields.Char(string="Monitoring Device ID", help="The id of this device that is assigned via the external monitoring system")
    monitoring_url = fields.Char(string="Monitoring Device URL", help="The direct url to the device in the external monitoring system")
    monitoring_status = fields.Boolean(string="Monitoring Status", help="Shows up (green), off (red) status from external monitoring system")
    rack = fields.Many2one('maintenance.equipment', string="Rack", help="Rack this equipment depends is installed in.")
    topo_url = fields.Char(string="Topo URL", help="Link to external topology tool.")

    #card equipment
    default_port_status = fields.Selection([('faulty', 'Faulty'),('in_service', 'In Service'),('out_of_service', 'Out of Service'),('un_equipped', 'Un-Equipped')], string="Default Port Status")
    card_type = fields.Selection([('normal', 'Normal'),('daughter_card', 'Daughter Card'),('mother_card', 'Mother Card')], string="Type")
    num_daughter_cards = fields.Integer(string="# of Daughter Cards")
    daughter_card_label_start = fields.Char(string="Label Start", help="Daughter Slot Label")
    card_size = fields.Selection([('one', '1 Slot'),('half', '1/2 Slot'),('fourth', '1/4 Slot'),('sixth', '1/6 Slot'),('two', '2 Slot'),('three', '3 Slot'),('four', '4 Slot')], string="Size")
    port_definitions = fields.One2many('equipment.portdefinition', 'card', string="Port Definitions")
    slot = fields.Many2one('equipment.slot', string="Slot")
    #rack equipment
    style = fields.Selection([('two_post_open_frame', '2 Post Open Frame'),('four_post_open_frame', '4 Post Open Frame'),('enclosed', 'Enclosed')], string="Style")
    color = fields.Selection([('aqua', 'Aqua'),('black', 'Black'),('blue', 'Blue')], string="Color")
    lockable = fields.Boolean(string="Lockable")
    stackable = fields.Boolean(string="Stackable")
    rear_mount = fields.Boolean(string="Rear Mount?")
    mounting_position = fields.Selection([('floor', 'Floor'),('wall', 'Wall')], string="Mounting Position")
    rack_units = fields.Integer(string="Rack Units")
    width = fields.Char(string="Width")
    depth = fields.Char(string="Depth")
    height = fields.Char(string="Height")
    equipment_width = fields.Char(string="Equipment Width")
    description = fields.Text(string="Description")
    #shelf equipment
    ru_size = fields.Char(string="RU Size")
    #pluggable equipment
    pluggable_type = fields.Many2one('equipment.pluggabletype', string="Type")
    #panel equipment
    panel_type = fields.Many2one('equipment.paneltype', string="Type")
    port_count = fields.Integer(string="Port Count")
    nomenclature = fields.Selection([('bidirectional', 'Bidirectional'),('free_form', 'Free Form'),('odds_evens', 'Odds and Evens'),('range', 'Range'),('vertical', 'Vertical')], string="Nomenclature")
    rows_of_ports = fields.Integer(string="Rows of Ports")
    installed = fields.Boolean(string="Installed")
    notes = fields.Text(string="Notes")
    is_carrier_panel = fields.Boolean(string="Is Carrier Panel?")
    #cage equipment
    audit_complete = fields.Boolean(string="Audit Complete")
    door_side = fields.Selection([('east', 'East'),('north', 'North'),('south', 'South'),('west', 'West')], string="Door Side")
