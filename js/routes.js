import Calendar from './calendar';
import Checklist from './checklist';
import Communication from './communication';
import Dropbox from './dropbox';


const routes = [
  {
    path: '/calendar',
    component: Calendar
  },
  {
    path: '/checklist',
    component: Checklist
  },
  {
    path: '/communication',
    component: Communication
  },
  {
    path: '/dropbox',
    component: Dropbox
  }
];

export { routes };