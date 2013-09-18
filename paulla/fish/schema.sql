create table if not exists tasks (
    id integer primary key autoincrement,
    fdescr char(100) not null,
    fpath char(100) not null,
    fid char(100) not null,
    fname char(100) not null,
    closed bool not null
);

/**
insert or ignore into tasks (id, fdescr, fpath, fid, fname, closed) values (0, 'Description01', './tasks/upfiles', 'c28787dd-17c2-4788-a5b2-d9619f7ab201', 'test_file01.txt', 0);
insert or ignore into tasks (id, fdescr, fpath, fid, fname, closed) values (1, 'Description02', './tasks/upfiles', 'c28787dd-17c2-4788-a5b2-d9619f7ab202', 'test_file02.txt', 0);
insert or ignore into tasks (id, fdescr, fpath, fid, fname, closed) values (2, 'Description03', './tasks/upfiles', 'c28787dd-17c2-4788-a5b2-d9619f7ab203', 'test_file03.txt', 0);
/**/
