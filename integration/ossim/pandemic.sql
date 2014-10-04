-- pandemic
-- plugin_id: 9099

DELETE FROM plugin WHERE id = "9099";
DELETE FROM plugin_sid where plugin_id = "9099";

INSERT IGNORE INTO plugin (id, type, name, description) VALUES (9099, 1, 'pandemic', 'Pandemic allows us to process pathogen detection like information security events');

INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 1, NULL, NULL, 'pandemic: Ebolavirus ' ,5, 5);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 2, NULL, NULL, 'pandemic: MRSA' ,5, 5);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 3, NULL, NULL, 'pandemic: Anthrax' ,5, 5);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 4, NULL, NULL, 'pandemic: Salmonella' ,3, 2);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 5, NULL, NULL, 'pandemic: Meningitis' ,3, 3);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 6, NULL, NULL, 'pandemic: Gonorrhea' ,3, 2);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 7, NULL, NULL, 'pandemic: Chlamydia' ,3, 2);

INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 8, NULL, NULL, 'pandemic: Rhinovirus' ,2, 2);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 9, NULL, NULL, 'pandemic: Influenza' ,2, 2);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 10, NULL, NULL, 'pandemic: Coronavirus' ,2, 2);
INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (9099, 11, NULL, NULL, 'pandemic: Staph' ,2, 2);
