import Calendar from './calendar';
import Checklist from './checklist';
import Communication from './quizzes';
import Config from './config';
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
    path: '/config',
    component: Config
  },
  {
    path: '/dropbox',
    component: Dropbox
  }
];

export { routes };